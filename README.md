# cowin

A simple python function that calls Government's ApiSethu Cowin portal to get available vaccine slots near you.
It takes a list of pincodes and age(18/45) as input and provides a list of hospitals and number of slots available for that age group in the area belonging to pincodes.
It also generated an alarm sound whenever there is an availability. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requests
pip install playsound
```

## Usage

```bash
python main.py
```
Enter the age group 18/45: 45

Please enter pincode (if there are no more pincode, press enter.):400703

Please enter pincode (if there are no more pincode, press enter.):400705

Please enter pincode (if there are no more pincode, press enter.):
