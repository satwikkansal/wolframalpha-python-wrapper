# wolframalpha-python-wrapper
A python wrapper for search api of WolframAlpha

#Usage
- Get your key from [here](http://www.wolframalpha.com/)
- Place `api.py` in your project folder and then use `import api` to add it to your main project file.
- Pass your query to  `api.get_json()` method and recieve the results in json format.

Sample results for the query `NaCl`

`[
  {
    "data": "sodium chloride",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28851efh634fdha182b0000067e2h51ib927hc2c?MSPStoreType=image/gif&s=39",
    "caption": "Input interpretation"
  },
  {
    "data": "formula | NaCl Hill formula | ClNa name | sodium chloride",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28861efh634fdha182b000001bb0bgc7hgg4a614?MSPStoreType=image/gif&s=39",
    "caption": "Chemical names and formulas"
  },
  {
    "data": "",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28871efh634fdha182b0000025dbbc9250d5353i?MSPStoreType=image/gif&s=39",
    "caption": "Structure diagram"
  },
  {
    "data": "molar mass | 58.443 g/mol phase | solid  (at STP) melting point | 801 °C boiling point | 1413 °C density | 2.16 g/cm^3 solubility in water | soluble",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28881efh634fdha182b0000060g5b4ba1688983c?MSPStoreType=image/gif&s=39",
    "caption": "Basic properties"
  },
  {
    "data": "density | 2.16 g/cm^3 vapor pressure | 0.9998 mmHg  (at 865 °C)",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28901efh634fdha182b000003ag1c592d4efcfac?MSPStoreType=image/gif&s=39",
    "caption": "Solid properties (at STP)"
  },
  {
    "data": "specific heat capacity c_p | solid | 0.8641 J/(g K) specific free energy of formation Delta_fG° | solid | -6.572 kJ/g specific heat of formation Delta_fH° | solid | -7.036 kJ/g specific entropy S° | solid | 1.232 J/(g K) specific heat of fusion | 0.4818 kJ/g |   (at STP)",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28921efh634fdha182b0000024i02a0e8beabhdd?MSPStoreType=image/gif&s=39",
    "caption": "Thermodynamic properties"
  },
  {
    "data": "CAS number | 7647-14-5 Beilstein number | 3534976 PubChem CID number | 5234 PubChem SID number | 24852266",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28941efh634fdha182b000001cgf17h8i80179i4?MSPStoreType=image/gif&s=39",
    "caption": "Chemical identifiers"
  },
  {
    "data": "",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28951efh634fdha182b000004f49cdcah4e96d4e?MSPStoreType=image/gif&s=39",
    "caption": "NFPA label"
  },
  {
    "data": "odor | odorless lethal dosage | 3000 mg/kg  (oral dose for rats)",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28961efh634fdha182b000003ehc90gg4ab2cgg4?MSPStoreType=image/gif&s=39",
    "caption": "Toxicity properties"
  },
  {
    "data": "Na^(+) (sodium) | 1 Cl^(-) (chloride) | 1",
    "image": "http://www4c.wolframalpha.com/Calculate/MSP/MSP28981efh634fdha182b000004ihi0062967589ic?MSPStoreType=image/gif&s=39",
    "caption": "Ion equivalents"
  }
]`
