# evaluation
import h5py


def evaluate():
    filename = ""  # h5 result file

    with h5py.File(filename, "r") as f:
        for key in f.keys():
            print(key) #Names of the groups in HDF5 file.
        
        #Get the HDF5 group
        group = f['df_with_missing']

        #Checkout what keys are inside that group.
        for key in group.keys():
            print(key)

        evaluation_result = group['table'][()]
        print(evaluation_result)

    gt_file = ''  # gt file
    gt = list()
    with open(gt_file, 'r') as fin:
        idx = 0
        for line in fin:
            if idx > 2:
                line = line.strip().split(',')
                gt.append(line)
            idx += 1

    # input the training index and test index, outputted from DeepLabCut
    test_idx = []
    train_idx = []

    pix_err_train = list()
    pix_err_test = list()
    img_idx_train = list()
    img_idx_test = list()

    def get_err(idxs):
        pix_err = list()
        img_idx = list()
        for idx in idxs:
            output = evaluation_result[idx]
            label = gt[idx]

            output_xyp = list(output[1])
            label_xy = []
            for item in label[1:]:
                if item:
                    label_xy.append(float(item))
                else:
                    label_xy.append(0)

            for i in range(9):
                x, y, p = output_xyp[3*i:3*i+3]
                gx, gy = label_xy[2*i:2*i+2]
                if p > 0.8:
                    err = np.linalg.norm([x-gx, y-gy])
                    if err < 550:
                        pix_err.append(err)
                        img_idx.append(idx)
        
        return pix_err, img_idx

    pix_err_train, img_idx_train = get_err(train_idx)
    pix_err_test, img_idx_test = get_err(test_idx)
    split_train = len(pix_err_train)*['train']
    split_test = len(pix_err_test)*['test']


    # plotting
    plotting = False
    if plotting:
        pix_err = pix_err_train + pix_err_test
        img_idx = img_idx_train + img_idx_test
        split = split_train + split_test

        ddata = {'pixel_error': err, 'image_index': img_idx, 'split': split} 
        df = pd.DataFrame(ddata)

        pix_err_df = pd.DataFrame(list(zip(pix_err, img_idx)), columns =['test', 'image_index'])


        alt.Chart(df).mark_circle(size=60).encode(
            #x='pixel_error',
            alt.X('pixel_error',
                scale=alt.Scale(domain=(0, 200))
            ),
            y='image_index',
            color='split'
        ).interactive()
