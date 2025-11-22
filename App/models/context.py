from App.models.application_state  import ApplicationState

class Context():
    def __init__(self,initialState:ApplicationState):
        self.state = initialState  # should have initial state when created because we accept an ApplicationState
        self.state.set_context(self)

    def setState(self,state:ApplicationState):
        self.state = state
        self.state.set_context(self)
    
    def next(self):
        self.state.next() # because we use the current state's methods to evoke some action
    
    def previous(self):
        self.state.previous()

    def getStateName(self):
        self.state.getStateName()
    
    def withdraw(self):
        self.state.withdraw()
    
    def getMatchedCompanies(self):
        self.state.getMatchedCompanies()