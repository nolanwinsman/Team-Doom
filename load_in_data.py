
#class common parameters
#put all parameters in there
#import module to baseline.py

class default_data:
    def __init__(self):
        #whoever is running this code make sure you change the name to your first name
        self.user = "Tim"

        # Game scenario 
        self.scenario = 'health_gathering_supreme'
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

        self.numEvaluations = 5
        self.save_model = True
        self.load_model = True
        self.skip_learning = True
        self.skip_evaluation = False #added line
        self.game_window_visible = True
        self.model_savefile = "./model-doom.pth"
        self.model_loadfile = "./models/model_basic_epochs_20_index_1/model_basic_epoch_0.pth" #set to a model pth file

    