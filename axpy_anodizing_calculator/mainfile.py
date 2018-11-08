import argparse
import sys

def main():

    '''Console script'''
    parser = argparse.ArgumentParser()

    # An argument without - is required
    parser.add_argument('surfacearea', type=float, help='Surface area in mm^2')
    parser.add_argument('-thickness', type=float, default=1, help='The anodizing thickness in "mils"')
    parser.add_argument('-currentdensity', type=float, default=0.15, help='The current density, default is 0.15 Amp/in^2')

    # Show help if no arguments are given
    if len(sys.argv) <=1:
        sys.argv.append('--help')

    args = parser.parse_args()

############################################################
    
    inch_per_mm = 0.0393700787

    squareinch = args.surfacearea*inch_per_mm**2
    setcurrent = squareinch * args.currentdensity
    #time =  720 * args.thickness / args.currentdensity
    time = 2 # TEMP
    peakvoltage = 2.5 * args.currentdensity
    print ('\033[91m')
    print('='*40) 
    print('          Anodizing recipie')
    print('          Axel Johansson V1.3')
    print('='*40)
    print ('\033[0m')    
    print(' Part Surface Area:\033[4m\t%.1f\033[0m mm^2 \n\n Set Current:\033[4m\t\t%.2f\033[0m Ampere\n Time:\t\t\t%.1f Hours\n Peak voltage:\t\t%.1f Vdc' % (args.surfacearea, setcurrent, time,peakvoltage))
    print('-'*40)
    print(' REMEMBER:\n (+) Goes to the part\n (-) Goes to the Cathode')
    print('-'*40)
    print('')
    #print ('\033[0m')
###########################################################    
if __name__ == "__main__":
    main()
