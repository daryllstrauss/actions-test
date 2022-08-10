from app.main import main

import runpy


class Test_App:
    def test_main(self):
        main()

    def test_module(self):
        runpy.run_module("app.main", run_name="__main__")
