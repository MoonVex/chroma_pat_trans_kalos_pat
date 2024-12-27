import os
import os.path
import re

curpath = os.path.dirname(__file__).replace('\\','\\\\')

def string_reverse(arr):
     return arr[::-1]
     
def param_inital():
    global lineNo 
    global output_flag
    global data_out1
    global data_out2
    global data_out3
    global data_out4
    global cycle_counter
    global transed_data
    global aStringArr
    global aStringLen
    global aa
    global bb
        
    lineNo              = 0
    output_flag         = ''
    data_out1           = []
    data_out2           = []
    data_out3           = []
    data_out4           = []
    cycle_counter       = 0
    transed_data        = ''
    aStringArr          = []
    aStringLen          = 0
    aa       = 0    
    bb       = 0 


def trans():
    output_file = open(curpath + '\\transed\\trans_ctm.bat','w')        
    for filenames in os.listdir(curpath + '\\raw_data_file_part\\'):
        #print(curpath)
        output_file.write('oai_patcom -k ..\TestPlans -p ..\TestPlans -t ..\OTPLSrc -s  ms10561.soc 		 '+filenames[:-3:]+'.pat\n')
    output_file.write('pause\n')
    output_file.close()        
        
def plist():
    output_file = open(curpath + '\\transed\\plist_ctm.txt','w')        
    for filenames in os.listdir(curpath + '\\raw_data_file_part\\'):
        #print(curpath)
        output_file.write('GlobalPList ms10561_'+filenames[:-3:]+'_plist{\n'+'   Pat '+filenames[:-3:]+';\n}\n\n')
    output_file.write('\n\n\n\n\n')
    output_file.close()        
    
def tpl():
    output_file = open(curpath + '\\transed\\tpl_ctm.txt','w')        
    for filenames in os.listdir(curpath + '\\raw_data_file_part\\'):
        #print(curpath)
        output_file.write('ms10561.plist:ms10561_'+filenames[:-3:]+'_plist,\n')
    output_file.write('\n\n\n\n\n')
    output_file.close()        
        
        
for filenames in os.listdir(curpath + '\\raw_data_file_part\\'):
    
    #print(curpath)
    output_file = open(curpath + '\\transed\\' + filenames[:-4:]+ '.txt','w')

    param_inital()
        
    try:       
        input_file_1 = open( curpath + '\\raw_data_file_part\\' + filenames,'r')  
    except:
        print('Can\'t open the file!!!!') 
    else:
        output_file.write('''
PG_VCD {

PORDIS_0		=		0;
PADR_0			=		1;
PADM_0			=		2;
TRST_0		    =		3;
STROBE_0		=		4;
TCK_0			=		5;
TDO_0			=		6;
TDI_0		    =		7;
VPP_0		    =		8;


STROBE_1		=		9;
TCK_1			=		10;
TDO_1			=		11;
TDI_1		    =		12;
VPP_1		    =		13;

STROBE_2		=		14;
TCK_2			=		15;
TDO_2			=		16;
TDI_2		    =		17;
VPP_2		    =		18;

STROBE_3		=		19;
TCK_3			=		20;
TDO_3			=		21;
TDI_3		    =		22;
VPP_3		    =		23;


PORDIS_4		=		24;
PADR_4			=		25;
PADM_4			=		26;
TRST_4		    =		27;
STROBE_4		=		28;
TCK_4			=		29;
TDO_4			=		30;
TDI_4		    =		31;
VPP_4		    =		32;

STROBE_5		=		33;
TCK_5			=		34;
TDO_5			=		35;
TDI_5		    =		36;
VPP_5		    =		37;

STROBE_6		=		38;
TCK_6			=		39;
TDO_6			=		40;
TDI_6		    =		41;
VPP_6		    =		42;

STROBE_7		=		43;
TCK_7			=		44;
TDO_7			=		45;
TDI_7		    =		46;
VPP_7		    =		47;

 };
VectorChar {
    // char   f1   f2   
    // ----   ---- ---- 
          0 = G2L, G2L (0);
          C = G2H, G2L (0);
          1 = G2H, G2H (1);
          M = G2L, G2H (0);
          X = G2Z, G2Z (1); 
          L = DC,  ED  (0);  
          H = DC,  ED  (1); 
};

PG_PATTERN ''') 
        output_file.write(''.join(filenames[:-4:])+'     //'+''.join(filenames[:-4:])+'\n')
        output_file.write('''
{  ''')
        for line in input_file_1:
            lineNo += 1
            aStringArr  = line.replace('\n','').replace(' ','')  
            aStringLen  = len(aStringArr)          
            if aStringLen!=0:
                    if ('*' in aStringArr): 
                            Arr2 = re.split('[\*\,\;]',aStringArr)
                            #print(Arr2)
                            #print(ts_set)
                            #input()
                            #ts
                            if ('TS' in Arr2[2]):
                                ts_set=re.findall('\d+',Arr2[2])
                            output_file.write('(tset '+''.join(ts_set)+')\t')

                            #RPT
                            if ('RPT' in aStringArr):
                                    aa=re.search('RPT\d+',aStringArr[4:]).start()+7
                                    bb=re.search('RPT\d+',aStringArr[4:]).end()+4
                                    output_file.write('repeat\t'+''.join(str(int(aStringArr[aa:bb])-1))+'\t')
                            else:
                                    output_file.write('\t\t')
                            
                            #cycle
                            output_file.write('\"\t')
                            if len(Arr2[1]) == 14 :
                                Arr2[1] = Arr2[1][:8] + Arr2[1][-2]
                            cyc1 = Arr2[1][:4]
                            if Arr2[1][5] == '1':
                                cyc2 = Arr2[1][4] + 'C' + Arr2[1][6:]
                            else:
                                cyc2 = Arr2[1][4:]
                            output_file.write(''.join(cyc1)+''.join(cyc2)+'\t'+''.join(cyc2)+'\t'+''.join(cyc2)+'\t'+''.join(cyc2)+'\t')
                            output_file.write(''.join(cyc1)+''.join(cyc2)+'\t'+''.join(cyc2)+'\t'+''.join(cyc2)+'\t'+''.join(cyc2)+'\t')
                            output_file.write('''"	;	//''')
                            
                            #note
                            aStringArr  = line.replace(',','\t').replace(' ','\t').replace(';//','\t').replace('\n','').replace(';','')   
                            output_file.write(aStringArr)
                            if ('RPT' not in aStringArr):
                                output_file.write('\t\t')
                            if ('Vector' not in aStringArr):
                                output_file.write('\t\t\t')
                            output_file.write('\n')
            else:
                    output_file.write('\n')          
            #input()

    finally:
        output_file.write('''								


};

''')    
        input_file_1.close()
        output_file.close()
        
        
        
output_file = open(curpath + '\\transed\\trans_ctm.bat','w')        
for filenames in os.listdir(curpath + '\\raw_data_file_part\\'):
    
    #print(curpath)
    output_file.write('oai_patcom -k ..\TestPlans -p ..\TestPlans -t ..\OTPLSrc -s  ms10561.soc 		 '+filenames[:-3:]+'.pat\n')
    
output_file.write('pause\n')
output_file.close()        


#trans()        
#plist()        
#tpl()        
print('Press any key to end')            
input()