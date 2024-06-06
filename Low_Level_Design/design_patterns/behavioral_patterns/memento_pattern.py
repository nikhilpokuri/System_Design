class EditorMemento:
    """Memento"""
    def __init__(self, state):
        self.__state = state
    
    def get_saved_state(self):
        return self.__state

class TextEditor:
    """Originator"""
    def __init__(self) -> None:
        self.__text = ""
    
    def write(self, text:str):
        self.__text += text
    
    def get_current_state(self):
        return self.__text
    
    def save(self):
        return EditorMemento(self.__text)
    
    def restore(self, memento:EditorMemento):
        self.__text = memento.get_saved_state()

class EditorHistory:
    """CareTaker"""
    def __init__(self):
        self.__history = []
    
    def add_memento(self, memento:EditorMemento):
        self.__history.append(memento)
    
    def undo(self):
        """0-based index"""
        if self.__history:
            return self.__history.pop()

#client
editor = TextEditor()
history = EditorHistory()

editor.write("nikhil") # now editor has "nikhil"
editor.write("_pokuri") # now editor has "nikhil_pokuri"
memento1 = editor.save() 
history.add_memento(memento1) # SAVING "nikhil_pokuri" TO HISTORY
print("First Stage:",editor.get_current_state())

editor.write("_chowdary") # now editor has "nikhil_pokuri_chowdary"
editor.restore(history.undo()) # now editor has restored to previous state i.e., "nikhil_pokuri" 
editor.write("_cr") # now editor has "nikhil_pokuri_cr" and saving to history
memento2 = editor.save() 
history.add_memento(memento2) # SAVING "nikhil_pokuri_cr" TO HISTORY
print("Second Stage:",editor.get_current_state())

editor.write("_chowdary") # now editor has "nikhil_pokuri_cr_chowdary"
editor.restore(history.undo()) # now editor has restored to previous state i.e., "nikhil_pokuri_cr" 
editor.write("_cse") # now editor has "nikhil_pokuri_cr_cse" and saving to history
memento3 = editor.save() 
history.add_memento(memento3) # SAVING "nikhil_pokuri_cr" TO HISTORY
print("Third Stage:",editor.get_current_state())

editor.restore(memento1) # now editor has restored to first state i.e., nikhil_pokuri
print("Final Stage(RESTORED TO FIRST):",editor.get_current_state())