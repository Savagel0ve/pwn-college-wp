import IPython
py = IPython.get_ipython()
py.Completer.use_jedi = False
py.Completer.greedy = True
