# -*- coding: utf-8 -*-

import argparse
import sys

#
# DEFINE YOUR FUNCTIONS HERE...
#

    
def main():

    '''Console script'''
    parser = argparse.ArgumentParser()

    # An argument without - is required
    parser.add_argument('surfacearea', type=float, help='Surface area in mm^2')
    parser.add_argument('-thickness', type=float, default=1, help='The anodizing thickness in "mils"')
    parser.add_argument('-currentdensity', type=float, default=6, help='The current density, default is 6 Amp/Ft^2')
    

    
    if len(sys.argv) <=1:
        sys.argv.append('--help')

    # Show help if no arguments are given
    args = parser.parse_args()


    # This formula is based on the "720 rule"

    inch_per_foot = 0.00328084

    squarefoot = args.surfacearea*inch_per_foot*inch_per_foot
    setcurrent = squarefoot * args.currentdensity
    time =  720 * args.thickness / args.currentdensity
    peakvoltage = 2.5 * args.currentdensity
    
    print(' Anodizing recipie')
    print('-'*30)

    print(' Part Surface Area: \t%.1f mm^2\n\n Set Current:\t\t%.2f Ampere\n Time:\t\t\t%.1f Minutes\n Peak voltage:\t\t%.1f Vdc' % (args.surfacearea, setcurrent, time,peakvoltage))
    print('-'*30)

    
if __name__ == "__main__":
    main()
