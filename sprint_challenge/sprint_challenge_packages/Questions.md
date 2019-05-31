# Acme Corporation Questionnaire 
<br>

What, in your opinion, is an important part of code reviews? That is, what is something you pay attention to when you review code, and that you appreciate when others do the same for your code? <br> <br>

The most important part of code reviews is to give constructive feedback to the reviewee that is designed to help them write cleaner, more readable, and more reproducable code in the future. A code review helps both the reviewer and the reviewee. When I am reading somebody elses code and I see patterns that inhibit my ability to read and understand the code, I begin to understand the importance of having clean code myself. Often times with code reviews, I see mistakes that I commonly make in the code of the reviewee. <br>

When I am reviewing code, the first thing I pay attention to is the docstrings and comments. Did the reviewee write down enough information so that I can understand what is going on without delving too deeply into the code itself? I appreciate when others point out when my documentation is unambiguous and lacking. It is important not only for others but also for my future self.


We have an awful lot of computers here, and it gets pretty confusing with slightly different things running on all of them. How could containers help us improve this situation? <br> <br>

Containers are particularly useful for the scenario described above. A container can create a completely standardized environment. The application, dependencies, libraries and all configurations will all be bundled together. If you are working on a big project with multiple team members contributing and the environment from machine to machine is not identical, problems will arise. Using containerized environments become increasingly necessary as a project increases in size and scope.