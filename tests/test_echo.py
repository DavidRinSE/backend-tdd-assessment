#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
from echo import create_parser, get_text

# Your test case class goes here

text = "Hello World."


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("./USAGE", "r") as f:
            usage = f.read()
            self.assertEquals(stdout, usage)

    def test_upper(self):
        # Testing the '-u' flag for upper
        u_parsed = self.parser.parse_args(['text', '-u'])
        self.assertTrue(u_parsed.upper)
        # Testing the '--upper' flag for upper
        upper_parsed = self.parser.parse_args(['text', '--upper'])
        self.assertTrue(upper_parsed.upper)

        # Testing the get_text function for upper
        self.assertEqual(get_text(text, upper=True), text.upper())

        process = subprocess.Popen(
            ["python", "./echo.py", "-u", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text.upper() + '\n')

    def test_lower(self):
        # Testing the '-l' flag for lower
        l_parsed = self.parser.parse_args(['text', '-l'])
        self.assertTrue(l_parsed.lower)
        # Testing the '--lower' flag for lower
        lower_parsed = self.parser.parse_args(['text', '--lower'])
        self.assertTrue(lower_parsed.lower)

        # Testing the get_text function for lower
        self.assertEqual(get_text(text, lower=True), text.lower())

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text.lower() + '\n')

    def test_title(self):
        # Testing the '-t' flag for title
        t_parsed = self.parser.parse_args(['text', '-t'])
        self.assertTrue(t_parsed.title)
        # Testing the '--title' flag for title
        title_parsed = self.parser.parse_args(['text', '--title'])
        self.assertTrue(title_parsed.title)

        # Testing the get_text function for title
        self.assertEqual(get_text(text, title=True), text.title())

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text.title() + '\n')

    def test_no_args(self):
        # Testing the text arg
        text_parsed = self.parser.parse_args(['Hello world.'])
        self.assertEqual(text_parsed.text, 'Hello world.')

        # Testing the get_text function
        self.assertEqual(get_text(text), text)

        process = subprocess.Popen(
            ["python", "./echo.py", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text + '\n')

    def test_many_args(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-tul", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text.title() + '\n')

        process = subprocess.Popen(
            ["python", "./echo.py", "-ul", text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout, text.lower() + '\n')


if __name__ == '__main__':
    unittest.main()
