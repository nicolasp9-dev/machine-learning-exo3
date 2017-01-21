#!/bin/bash

echo "ISMIR Genre datasets"
echo ""
echo "ISMIR Genre.rp :"
python exo_3_code.py -d ISMIRgenre/ISMIRgenre.rp.arff
echo ""
echo "ISMIR Genre.rh :"
python exo_3_code.py -d ISMIRgenre/ISMIRgenre.rh.arff
echo ""
echo "ISMIR Genre.ssd :"
python exo_3_code.py -d ISMIRgenre/ISMIRgenre.ssd.arff

echo ""
echo "--------"
echo ""

echo "GTZAN datasets"
echo ""
echo "GTZAN.rh"
python exo_3_code.py -d GTZAN/GTZAN_O.rh.arff
echo ""
echo "GTZAN.rp"
python exo_3_code.py -d GTZAN/GTZAN_O.rp.arff
echo ""
echo "GTZAN.ssd"
python exo_3_code.py -d GTZAN/GTZAN_O.ssd.arff

echo ""
echo "--------"
echo ""

echo "ISMIRrhythm datasets"
echo ""
echo "ISMIRrhythm.rh"
python exo_3_code.py -d ISMIRrhythm/ISMIRrhythm.rh.arff
echo ""
echo "ISMIRrhythm.rp"
python exo_3_code.py -d ISMIRrhythm/ISMIRrhythm.rp.arff
echo ""
echo "ISMIRrhythm.ssd"
python exo_3_code.py -d ISMIRrhythm/ISMIRrhythm.ssd.arff

echo ""
echo "--------"
echo ""

echo "LMD datasets"
echo ""
echo "LMD.rh"
python exo_3_code.py -d LMD/LMD.rh.arff
echo ""
echo "LMD.rp"
python exo_3_code.py -d LMD/LMD.rp.arff
echo ""
echo "LMD.ssd"
python exo_3_code.py -d LMD/LMD.ssd.arff
echo ""
echo "LMD.tssd"
python exo_3_code.py -d LMD/LMD.tssd.arff
