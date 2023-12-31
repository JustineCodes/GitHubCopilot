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
- When you create a function in the script then go to use it later on, Copilot will fill in the parameters and variables. Wicked helpful.

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

- Monday the 3rd of July
  - I was thinking about trying for the 100 days of coding, but I like not being on the computer on weekends too much for that. :)
  - Today I started looking into how to use Nightfall as DLP for my AI ChatGPT script. I so how it works, but still grasping at how to get it to work. Nightfall looks to have good documentation to help me figure this out.
  - I know I'll figure it out.

- Tuesday the 4th of July
  - I was able to create a nightfallTest.py that warned me if credit card numbers where being used. I find the error to be in a strange formate, but it seems to work.
  - Then Copilot decided to stop printing python code out in codeblocks and became rather useless to me.
  - I'm now working through how to have the code scanned by Nightfall first. If that fails the DLP test, then nothing gets sent to ChatGPT.
  - Work until you hit a block, then pause, think, and come back.
  
- Wednesday the 5th of July
  - I found this helpful [Python Example](https://www.nightfall.ai/blog/chatgpt-dlp-filtering-how-to-use-chatgpt-without-exposing-customer-data#python-example), and have it working in a script of it's own. But learning to understand how it works, and migrate it into a script I have is interesting.
  - And it's working in my code.
  - I'm happy that I'm progressing with this project. But still concerned I'm not learning as much Python as I would like. The goals are being met, and that is the important part.
  - At work today in PowerShell I was able to turn a comment into code through Copilot. It was pretty cool. I wrote out what I needed to happen, and Copilot gave me working code. I made some minor adjustments, mostly due to preference on how I want my code to look and work, but the base script it produced, did the job.

- Thursday the 6th of July
  - I'm moving in two weeks, and had some changes at work that require my focuses. This is a fun learning process, and I'm enjoying myself. However, it's not my top priority in life. I'll do what I can when I can.
  - Side thought time
    - I also find myself at an interesting crossroad. While I need to keep my "day job" (day-to-Day bills, right?) I find myself asking myself, "Is the company pushing me in the direction I want to go? I am forever thankful that they like me enough to want me to stay. To allow me to change positions, and not tell me to leave. But, will my lack of direction put me somewhere I don't want to be in the future? I have skills today that I didn't have a few years ago. This gives me choices. I can work for something else, while I do a good job and gain experience in the role they ask me to do. I can treat it as a fun learning opportunity, while I work toward something else on my time. It may be time for me to depend less on what my current employer wants, and more on what I want. Time to work on my self confidence and chase a dream or two. It seems getting a little stability in life has made me fearful of losing it. But without risk, is there ever a gain?

- Tuesday the 11th of July
  - I have been getting lots of use out of Copilot at work with PowerShell. I enjoy seeing solutions that I may not have thought of. The inline prediction is pretty neat, and has helped me improve my spelling.
  - I still type out most code, but I find the prediction helps me spell the commands correctly. I also love how it fills in a function, with parameters, when I call it further down in the script.

- Thursday the 13th of July
  - Today I started digging into how Jira works. I find GUIs interesting as you need to learn how to navigate the software. Where as with the command line you learn to talk to it.With a stroke of luck though I was able to help someone else learn a bit about Jira and sprints. I find sharing my knowledge helps me learn and better understand. Its the explaining what I learned that helps solidify the new information.
    - I was able to backup and restore my test environment.
    - Learned the difference between company managed and Team managed. I see why we are going with company managed.
    - I really want to better understand creating flows for each project. We currently have one flow for all projects, and that doesn't really work well. Tomorrow I think I'll focus on flow creation.
  - This evening I have been reading up on Power Platform administration. It is a bit overwhelming to be learning two things at once. But I have been a bit of a slacker the past year, so I don't mind. Lots of new terms and concepts that I'm wrapping my head around.
    - It's neat that there are different types of environments to use. I thought it was just a label, but nope, each environment has a purpose.
    - Permissions are something I'm going to need to invest a bit of time into. I want to thoroughly understand what gives what.
    - I like how you can use environments as containers for different people to store information and apps.