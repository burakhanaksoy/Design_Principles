<h1>Cohesion</h1>

<p align="center">
  
  <img width="450" height="350" src="https://user-images.githubusercontent.com/31994778/122711571-0ad50b80-d26b-11eb-99cd-6c702713eeed.png">
  
</p

<b>Cohesion is a metric of how good `Single Responsibility Principle`, a.k.a `Separation of Concerns` is implemented in design. Low cohesion means `SRP` is broken - modules are unfocused and they are doing way more than than they are supposed to.</b>
  
  Example of low cohesion(bad):
  
  ```
  -------------------
| Staff           |
-------------------
| checkEmail()    |
| sendEmail()     |
| emailValidate() |
| PrintLetter()   |
-------------------
```
 
 Example of high cohesion(good):
 
 ```
 ----------------------------
| Staff                   |
----------------------------
| -salary                 |
| -emailAddr              |
----------------------------
| setSalary(newSalary)    |
| getSalary()             |
| setEmailAddr(newEmail)  |
| getEmailAddr()          |
----------------------------
```

In the first example, Staff class' job(responsibility) is not `checkEmail()`, `sendEmail()`, `emailValidate()`, and so on.. 

It's main responsibility is to:

- Contain necessary properties related to a staff member.
- Set getters and setters for the properties of a staff member.
- Construct a staff member.

Credits to: [here](https://stackoverflow.com/questions/3085285/difference-between-cohesion-and-coupling)

<h1>Coupling</h1>

<b>Coupling is the metric for measuring how interrelated the blocks, classes, modules of the design is.</b>

<p>
<strong>Loose Coupling:</strong>
  Good one. The more loosely coupled our design, the less interrelated our code, hence the less dependence between the parts, hence the better implementation of SOLID principles.
</p>
<p>
<strong>Tight Coupling:</strong>
  Bad one. The more tightly coupled our design, the more interrelated our code, hence the more dependence between the parts, hence the worse implementation of SOLID principles.
</p>

>For low coupled classes, changing something major in one class should not affect the other. High coupling would make it difficult to change and maintain your code; since classes are closely knit together, making a change could require an entire system revamp.

<h2>Summary</h2>

- High cohesion and loose coupled design is preferred.
  - Makes the code more scalable and maintainable.
- Cohesiveness and Coupling has no measurable value.
- We cannot fully rid of Coupling due to `Composition` being an important part of OOP.
