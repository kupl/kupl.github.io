+++
draft = false
title ={{ $name_list := split .File.Dir "/" }}'{{ print (index $name_list 1) " " (index $name_list 2) | upper }}'
name = 'course name'
+++

# Course Name

## Course Information

## References

## Slides

## Homework