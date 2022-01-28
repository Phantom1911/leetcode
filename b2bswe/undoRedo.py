class Solution:
    def performEditorActions(self, actions):
        '''
        :type actions: list of list of str
        :rtype: str
        '''
        '''
        perform an action and put it into undo stack
        to undo, pop element from the undo stack and put it in the redo stack
        '''
        print(actions)
        undoStack, redoStack, currStr = [], [], ""
        for action in actions:
            if not undoStack:
                if action[0] == 'REDO' or action[0] == 'DELETE' or action[0] == 'UNDO':
                    continue
                if action[0] == 'INSERT':
                    currStr += action[1]
                    undoStack.append(Action('INSERT', currStr))
            else:
                if action[0] == 'INSERT':
                    currStr += action[1]
                    undoStack.append(Action('INSERT', currStr))
                elif action[0] == 'DELETE':
                    currStr = currStr[:-1]
                    undoStack.append(Action('DELETE', currStr))
                elif action[0] == 'UNDO':
                    lastAction = undoStack.pop()
                    currStr = undoStack[-1].strAfterAction
                    redoStack.append(lastAction)
                elif action[0] == 'REDO':
                    if not redoStack:
                        continue
                    lastAction = redoStack.pop()
                    undoStack.append(lastAction)
                    currStr = undoStack[-1].strAfterAction

        return undoStack[-1].strAfterAction


class Action:
    def __init__(self, action, strAfterAction):
        self.action = action
        self.strAfterAction = strAfterAction

if __name__=="__main__":
    print(Solution().performEditorActions([["INSERT","a"],["INSERT","b"],['UNDO'],['REDO'],['REDO']]))