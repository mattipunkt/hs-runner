# Haskell Code-Runner
This is an attempt to build a Code-Runner module for running Haskell-Code in the Code-Runner-Extension for Moodle2 by sending web-requests to a FastAPI-Server, running the declarations in GHCi and returning the result, or the error.

This will only work if Moodle's CodeRunner-Extensions allows networking outside of the sandbox.