
#class common parameters
#put all parameters in there
#import module to baseline.py

class default_data:
    def __init__(self):
        #whoever is running this code make sure you change the name to your first name
        self.user = "Nolan"

        # Game scenario 
        self.scenario = 'defend_the_center'
        self.config_file_path = "scenarios/"+self.scenario+".cfg"
        
        # Q-learning settings
        self.epochs = 20
        self.learning_rate = 0.00025
        self.discount_factor = 0.99
        self.learning_steps_per_epoch = 2000
        self.replay_memory_size = 10000

        # NN learning settings
        self.batch_size = 64

        # Training regime
        self.test_episodes_per_epoch = 100

        # Other parameters
        self.frame_repeat = 12
        self.resolution = (30, 45)
        self.episodes_to_watch = 10

        self.save_model = True
        self.load_model = False
        self.skip_learning = False
        self.skip_evaluation = True #added line
        self.game_window_visible = True
        self.model_savefile = "./model-doom.pth"
        self.model_loadfile = "./model-doom.pth"

    