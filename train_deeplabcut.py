import deeplabcut

task = 'body_part_detection'
experimenter = ''
video = []  # list all the training videos
path_config_file=deeplabcut.create_new_project(task,experimenter,video,copy_videos=True)

path_config_file = ''

#AUTOMATIC:
deeplabcut.extract_frames(path_config_file)

#%gui wx
deeplabcut.label_frames(path_config_file)


deeplabcut.create_training_dataset(path_config_file)

# training
deeplabcut.train_network(path_config_file, saveiters=10000, maxiters=300000, gputouse=0)

# evaluation
deeplabcut.evaluate_network(path_config_file, plotting=True)

# Analyzing videos
videofile_path = ['E:\\pyWorkspace\\mouse_pose\\videos\\noTone.mp4'] #Enter a folder OR a list of videos to analyze.
deeplabcut.analyze_videos(path_config_file, videofile_path, gputouse=0, videotype='.mp4', save_as_csv=True)


# create labeled video
deeplabcut.create_labeled_video(path_config_file, videofile_path, videotype='mp4', fastmode=True, save_frames=False)

