# GitHubCopilot

<!-- In this repo I am learning how Github Copilot can help improve my coding. -->

## Table of Contents

- [Introduction](#introduction)
- [Positive](#Positive)
- [Lessons](#Lessons)
- [Thoughts](#Thoughts)
- [Notes](#notes)
  <!-- [Contributing](#contributing)
  - [Support](#support)
  - [License](#license) -->

## Introduction

This is a repository where I am learning how GitHub Copilot can help improve my coding. I think this is a fabulous tool, and am excited to watch it grow.

## Positive
- I'm finding the code prediction helpful.
- It has shown me working solutions that were better than what I was going to do.
- Having a chat option that is focused on code is a wonderful improvement to me workflow. Today I was able to get unstuck a few times by selecting the some code, and asking Copilot what it did, and why was I getting an error.
- I enjoy how it explains the error or selected code.

## Lessons
- Learning to talk to Copilot is an interesting art.
- In this current state I feel you still need a basic understanding of what you are doing. I have never coded in python and Copilot is helping with the learning curve. But it's not giving me answers like it does when I code in PowerShell.
- I am seeing how Copilot can help reduce the learning curve with learning new programming languages.

## Thoughts
  - I wonder how much Python programming I am learning. Or could this be the new way of coding? I learn how to ask the right questions, and AI creates the solution? This is probably also due to me not creating something new. I could probably have found this code on the internet.
    - I am learning python, just in a new way.
  - At work I find Copilot more helpful in resolving errors, than creating new scripts.

## Notes
- Tuesday the 27th of June
  - So somehow I got started trying to create a python chat with ChatGPT.
  - API set up, and hopefully I hide it in gitignore correctly.
  - Used Copilot and ChatGPT in the browser to create the code.
  - A number of errors, and the last one says. "openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details." So ya that's what's up today.

- Wednesday the 28th of June
  - The error means I need to set up a payment plan for use of the API. I thought it was part of the ChatGPT fee. I can do that.
  - Okay I set that up, still getting error. humm
  - Fixed it! I think I needed to wait a few for the billing part to start.
  - With the help of Copilot, I added a quit to my chat loop.
  - I have a rudimentary ChatGPT script in Python. Pretty cool.
  - I started building a GUI python script that I plan to build into something I can use to chat with ChatGPT.

- Thursday the 29th of June
  - I found <a href="https://freedomgpt.com/" target="_blank">FreedomGPT</a>
    it's supposed to run local, have less restrictions, and be more private. <a href="https://github.com/ohmplatform/FreedomGPT/" target="_blank">GitHub</a> has information.
  - So I have never used 11 GB of RAM on this laptop before. I see why the recommend 16GB RAM.
  - I like the theory, but not sure this laptop is can run the software very well.
  - Back to my AI Chatbot and Python learning.
  - Corrected my secrets file to a name that remove the conflict with python's standard library modules.
  - I now have a GUI for my ChatBot!
  - It was interesting, I asked Copilot, "How do I merge my AIChatBot.py with my TestGUI.py" and it showed me how. For some odd reason it did change my ChatGPT API engine, but once I updated that things worked as I expected.

- Friday the 30th of June
  - I added a filter to the user input. This prevents the user from using certain words when reaching out to ChatGPT. I am thinking this is one way that you could allow people to use ChatGPT and have a guardrails for data safety. Though for it to really work, the filter would need to be intelligent enough to read context. Like an AI filter for AI.
  - I will think on this a bit more.
  - Look and you will find [Nightfall](https://docs.nightfall.ai/), a software built for help implement DLP into your application. Incoming research time.


