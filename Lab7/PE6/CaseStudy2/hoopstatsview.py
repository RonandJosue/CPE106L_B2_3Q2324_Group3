"""
File: hoopsstatsview.py
The view for view and analyzing basketball player statistics.
"""

from breezypythongui import EasyFrame
import pandas as pd

class HoopStatsView(EasyFrame):

    def __init__(self, frame):
        """Creates and lays out window components
        to view and manipulate the model's data."""
        EasyFrame.__init__(self, title = "Basketball Stats")
        self.setSize(600, 400)
        self.frame = frame
        self.dataArea = self.addTextArea(text = self.frame.to_string(), 
                                         row = 0,
                                         column = 0,
                                         columnspan = 2,
                                         height = 15)
        # Create a panel for the radio buttons
        self.radioGroup = self.addRadiobuttonGroup(row = 1,
                                                   column = 0)
        defaultRB = self.radioGroup.addRadiobutton(text = "MIN")
        self.radioGroup.setSelectedButton(defaultRB)
        self.radioGroup.addRadiobutton(text = "FG%",
                                       command = self.analyze)
        self.radioGroup.addRadiobutton(text = "FT%",
                                       command = self.analyze)
        self.radioGroup.addRadiobutton(text = "REB",
                                       command = self.analyze)
        self.radioGroup.addRadiobutton(text = "AST",
                                       command = self.analyze)
        self.radioGroup.addRadiobutton(text = "PTS",
                                       command = self.analyze)
        # Create a panel for the output fields
        statsPanel = self.addPanel(row = 1, column = 1)
        statsPanel.addLabel("Mean", row = 0, column = 0)            
        statsPanel.addLabel("Median", row = 1, column = 0)                        
        statsPanel.addLabel("Standard deviation", row = 2,
                            column = 0)
        self.meanFld = statsPanel.addFloatField(value = 0.0,
                                                width = 5,
                                                row = 0,
                                                column = 1,
                                                precision = 2)            
        self.medianFld = statsPanel.addFloatField(value = 0.0,
                                                  width = 5,
                                                  row = 1,
                                                  column = 1,
                                                  precision = 2)            
        self.stdFld = statsPanel.addFloatField(value = 0.0,
                                               width = 5,
                                               row = 2,
                                               column = 1,
                                               precision = 2)                        
        self.analyze()
         
    # Event-handling method
    def analyze(self):
        """Updates the view with the results of analysis."""
        columnLabel = self.radioGroup.getSelectedButton()["text"]
        column = self.frame[columnLabel]
        self.meanFld.setNumber(column.mean())
        self.medianFld.setNumber(column.median())
        self.stdFld.setNumber(column.std())

    
