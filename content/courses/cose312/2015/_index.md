+++
draft = false
title = 'COSE312-15F'
+++

# Compilers, 2015 Fall

## Course Information

- Instructor: [Hakjoo Oh]({{< ref "/members/hakjoo-oh.md" >}})
- Lecture: 17:00-18:15 on Tuesdays and Thursdays
- Reference:
    {{< figure src="http://ecx.images-amazon.com/images/I/51Bug87tM+L._AA160_.jpg" width="150px" link="http://www.amazon.com/Compilers-Principles-Techniques-Tools-2nd/dp/0321486811/ref=sr_1_1?ie=UTF8&qid=1448024118&sr=8-1&keywords=compilers" target="_blank" >}}

## Slides

### Lectures

- Course Overview: [lec0.pdf](./slides/lec0.pdf)
- Structure of Compilers: [lec1.pdf](./slides/lec1.pdf)
- Lexical Analysis: [lec2.pdf](./slides/lec2.pdf) [lec3.pdf](./slides/lec3.pdf) [lec4.pdf](./slides/lec4.pdf) [lec5.pdf](./slides/lec5.pdf)
- Syntax Analysis: [lec6.pdf](./slides/lec6.pdf) [lec7.pdf](./slides/lec7.pdf) [lec8.pdf](./slides/lec8.pdf) [lec9.pdf](./slides/lec9.pdf) [lec10.pdf](./slides/lec10.pdf) [calc.tar](./code/calc.tar)
- Translation: [lec11.pdf](./slides/lec11.pdf) [lec12.pdf](./slides/lec12.pdf) [lec13.pdf](./slides/lec13.pdf)
- Optimization and Static Analysis: [lec14.pdf](./slides/lec14.pdf) [lec15.pdf](./slides/lec15.pdf) [lec16.pdf](./slides/lec16.pdf) [lec17.pdf](./slides/lec17.pdf) [lec18.pdf](./slides/lec18.pdf)
- Register Allocation: [lec19.pdf](./slides/lec19.pdf)
- Last: [lec20.pdf](./slides/lec20.pdf)

### Supplements

- [Overview of Static Analysis Research at KU](./slides/overview-sar.pdf)
- [Program Synthesis](slides/program-synthesis.pdf)
- [A Gentle Introduction to Program Analysis (by Isil Dillig)](./slides/dillig-plmw14.pdf)
- [What is static analysis? (by Matt Might)](https://matt.might.net/articles/intro-static-analysis/)

## Homework

- [HW1 (due 9/24)](./hw/hw1.pdf)
- [HW2 (due 10/15)](./hw/hw2.pdf)

## Project (Due 11/20, Fri)

1. [Project Page (GitHub)](https://github.com/hakjoooh/CompilerProject2015)
2. Clone the project package from GitHub (Clone url: https://github.com/hakjoooh/CompilerProject2015.git)
3. Complete four files: lexer.mll, parser.mly, translator.ml, and optimizer.ml
4. Submit the four files via Blackboard.
5. [score](./project-score.pdf)

## Exam

- [Mid](./mid.pdf)
- [Final](./final.pdf)

## Reference

- OCaml basics: [An introduction to OCaml](/courses/cose212/2015/slides/lec3.pdf), [Tutorial](https://ocaml.org/learn/tutorials/)
- [OCamllex](./ocamllex-tutorial.pdf) and [OCamlyacc](./ocamlyacc-tutorial.pdf)
- [An introduction to Git](http://rogerdudler.github.io/git-guide/)
- How to install OCaml programming environment
    - [Installing the Programming Environment (for Windows users)](./guide_ocaml_install.pdf)
    - VirtualBox Image (Ubuntu system with OCaml installed)
- Why ML?
    - [Who Teaches Functional Programming?](http://www.pl-enthusiast.net/2014/09/02/who-teaches-functional-programming/)
    - [Why finantial companies on Wall street often use OCaml?](http://www.infoq.com/presentations/jane-street-caml-ocaml)
    - [프로그래밍 교육에서 실습 언어의 선택](http://ropas.snu.ac.kr/~kwang/paper/position/edu.pdf)
    - [값 중심의 프로그래밍](http://ropas.snu.ac.kr/~kwang/paper/maso/1.pdf)