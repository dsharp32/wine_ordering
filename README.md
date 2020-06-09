# Ordering Wine with Python

A python3 program for compiling orders from a spreadsheet, generating a pdf purchase order and sending as email.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

You will need Python3 and microsoft Excel installed.

You will also need to write a python module called send_message.py with arguments email, order, company, body,po, cc_email, bcc_email.

The easiest option is to use the the ezgmail module by Al Sweigart. Instructions for utilizing it can be found here: 


https://automatetheboringstuff.com/2e/chapter18/

### Installing

Copy all files and folders to a folder of your choice.

Use order_sheet_2020.xlsx as an order template. As many blocks as needed can be made.

You need to close the excel file before running the program. This is very easy to forget to do!

run order.py in the command line.

## Testing

The easiest way to test is to replace the suppliers email address with your own and run.

## Built With

* [Anaconda](https://www.anaconda.com/products/individual)

## Author

* **Daniel Sharp** 

## License

This project is licensed under the MIT License 

## Acknowledgments

* Thanks to Al Sweigart for publishing ATBSWP free online. Make sure you support him and buy the 2nd Edition if you use it.
