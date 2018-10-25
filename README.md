# Simple Pharmacokinetic Model
The simplest possible mathematical model of drug concentration in blood plasma vs. time.

The model assumes exponential law. The higher the concentration level, the quicker this level is reducing over time.

There are two parameters to the model:

* Elimination half-life of the drug. For instance, if the half-life is 12 hours, it means that in 12 hours after we take a single pill the drug concentration in blood plasma is going to be equivalent to half the initial dose (half a pill).
* Dosing frequency. The dosing frequency of 24 hours means that we take a single pill periodically every 24 hours.

Elimination half-life is always written in the drug instruction and the dosing frequency is usually prescribed by doctors. This model gives very rough estimation of the effective accumulated concentration level of the drug over a large period of time (when it stabilizes).

# How to Use the Script
First, install the dependencies:

    python3 -m pip install -r requirements.txt

Show plot when the drug elimination half-life is 13 hours and the period between drug admission is 4 hours:

    ./plot.py 13 4

If you want to save the plot to a `.png` file, use the `--save` flag:

    ./plot.py 13 4 --save

# Results
There are three distinct drug admission scenarios that we are going to compare.

In the first example we model the case where the drug is administered more frequently than the drug elimination half-life period. This leads to high level of the drug concentration in blood plasma (almost 5 times the concentration level of a single pill). But the important part is that the concentration level stabilizes over time. The exponential nature of the process doesn't allow the drug concentration to grow indefinitely.

![Pic-13-4](/examples/pharmacokinetic-curve-13-4.png)

In the second example we model the scenario where we take one pill every 24 hours and the elimination half-life is 12 hours.

![Pic-12-24](/examples/pharmacokinetic-curve-12-24.png)

In the third example we take one pill every 48 hours and the half-life is 12 hours. In this case the drug concentration level drops almost to zero between drug administering moments because the administering period is quite large.

![Pic-12-48](/examples/pharmacokinetic-curve-12-48.png)
