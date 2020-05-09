from mycroft import MycroftSkill, intent_file_handler

class ReadStory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('story.read.intent')
    def handle_story_read(self, message):
        self.speak_dialog('story.read')
        with open('skills/read-story-skill/snoopy_at_the_dog_show.txt') as file_object:
            book = file_object.read()
            self.speak(book)
 
    def stop(self):
        pass

def create_skill():
    return ReadStory()
