'''
Created on 13 sept. 2017

@author: Fab
'''

import sqlite3
from database.Animal import *
import matplotlib.pyplot as plt
from database.Event import *
from database.Measure import *
from database import BuildEventTrain3, BuildEventTrain4, BuildEventTrain2, BuildEventFollowZone, BuildEventRear5, BuildEventFloorSniffing,\
    BuildEventSocialApproach, BuildEventSocialEscape, BuildEventApproachContact,BuildEventOralOralContact,\
    BuildEventApproachRear, BuildEventGroup2, BuildEventGroup3, BuildEventGroup4, BuildEventOralGenitalContact, \
    BuildEventStop, BuildEventWaterPoint, BuildEventSequentialRearing,BuildEventSequentialRearing2, \
    BuildEventMove, BuildEventGroup3MakeBreak, BuildEventGroup4MakeBreak,\
    BuildEventSideBySide, BuildEventSideBySideOpposite, BuildEventDetection,\
    BuildDataBaseIndex, BuildEventWallJump, BuildEventSAP,\
    BuildEventOralSideSequence
    
from tkinter.filedialog import askopenfilename
from database.TaskLogger import TaskLogger
import sys
import traceback

max_dur = 3*oneDay

class FileProcessException(Exception):
    pass

def process( file ):

    print(file)
    connection = sqlite3.connect( file )        
        
    #t = TaskLogger( connection )
    #t.addLog( "Rebuild all event launch" )
                
    try:
                        
        BuildDataBaseIndex.buildDataBaseIndex( connection, force=False )
        BuildEventDetection.reBuildEvent( connection, tmin=0, tmax=max_dur )
    
        BuildEventOralOralContact.reBuildEvent( connection, tmin=0, tmax=max_dur )        
        BuildEventOralGenitalContact.reBuildEvent( connection, tmin=0, tmax=max_dur )
        
        BuildEventSideBySide.reBuildEvent( connection, tmin=0, tmax=max_dur )        
        BuildEventSideBySideOpposite.reBuildEvent( connection, tmin=0, tmax=max_dur )        
    
        BuildEventTrain2.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventTrain3.reBuildEvent( connection, tmin=0, tmax=max_dur )   
        BuildEventTrain4.reBuildEvent( connection, tmin=0, tmax=max_dur )    
                 
        BuildEventMove.reBuildEvent( connection, tmin=0, tmax=max_dur )
           
        BuildEventFollowZone.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventRear5.reBuildEvent( connection, tmin=0, tmax=max_dur )
        
        BuildEventSocialApproach.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventSocialEscape.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventApproachRear.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventGroup2.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventGroup3.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventGroup4.reBuildEvent( connection, tmin=0, tmax=max_dur )
    
        BuildEventGroup4MakeBreak.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventGroup3MakeBreak.reBuildEvent( connection, tmin=0, tmax=max_dur )
    
        BuildEventStop.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventWaterPoint.reBuildEvent(connection, tmin=0, tmax=max_dur)
        BuildEventApproachContact.reBuildEvent( connection, tmin=0, tmax=max_dur )
        BuildEventWallJump.reBuildEvent(connection, tmin=0, tmax=max_dur)
        BuildEventSAP.reBuildEvent(connection,  tmin=0, tmax=max_dur)
    
        BuildEventOralSideSequence.reBuildEvent( connection, tmin=0, tmax=max_dur )
        
    except:
        
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        error = ''.join('!! ' + line for line in lines)
        
        t = TaskLogger( connection )
        t.addLog( error )
        
        print( error, file=sys.stderr ) 
        
        raise FileProcessException()
        

if __name__ == '__main__':
    
    print("Code launched.")
     
    files = askopenfilename( title="Choose a set of file to process", multiple=1 )
    
    for file in files:
        '''
        from multiprocessing.dummy import Pool as ThreadPool 
        pool = ThreadPool(4) 
        results = pool.map( process, files )
        pool.close()
        pool.join()
        '''
        try:
            process( file )
        except FileProcessException:
            print ( "STOP PROCESSING FILE " + file , file=sys.stderr  )
        
    print( "*** ALL JOBS DONE ***")
        
        