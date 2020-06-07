from mycroft import MycroftSkill, intent_file_handler, intent_handler
import time

class ReadStory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('story.read.intent')
    def handle_story_read(self, message):
        self.speak_dialog('story.read')
        response = self.get_response('Tell me the story you want to hear Snoopy at the dog show, Rock a Bye Snoopy, or Snoopys  Baseball Game', num_retries=-1)
        time.sleep(5)
        self.speak(response)

        if 'rock' in response:
            filename = 'skills/read-story-skill/rock_a_bye_snoopy.txt'
            self.speak('rock')
        elif 'show' in response:
            filename = 'skills/read-story-skill/dog_show.txt'
            self.speak('dog show')
        elif 'baseball' in response:
            filename = 'skills/read-story-skill/baseball_game.txt'
            self.speak('Snoopys baseball game')
        else:
            self.speak('You did not select a book so I will read you Snoopy at the dog show')
            filename = 'skills/read-story-skill/dog_show.txt'

        with open(filename) as file_object:
            book = file_object.read()
            self.speak('It may take a minute for me to find the story')
            self.speak(book)

    def stop(self):
        pass

def create_skill():
    return ReadStory()

 
