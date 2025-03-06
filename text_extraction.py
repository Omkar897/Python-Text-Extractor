import re


# Define a dictionary with desired key-value pairs and their patterns
desired_values = {
    "Patient Name": r"REHANA (.*?) Ref",
    "Age": r"Age: (\d+\.\d+) Years",
    "Sex": r"Sex: (.*?) Report",
    "Diagnosis": r"Diagnosis \:- (.*?)\n",
    "HPE No.": r"HPE no. : (.*?)\n",
}

# Extract text (assuming you already have the extracted text)
text = """
REHANA INAMDAR Ref: Dr.KOPPIKERC B MS(GS)

[Sample Collected At SID: 121349508
Orchids Speciality Breast Care Centre Collection Date:
FlatNo 1&2, Kapilvastu, SB Road, 14-03-2022 07:21 PM
REPORT Next to Ratna Hospital, Registration Date:
Pune 411016 Zone SHVA 14-03-2022 07:21 pm
Report Date:
Age: 54.00 Years Sex: FEMALE 16-03-2022 10:44 AM

HISTOLOGY

Operated case of left breast carcinoma. Now, discharge from scar and hardening. ?1
necrosis, ?recurrence. Mild FDG avid on PET.

Clinical details :
Nature ofspecimen: Biopsy from left breast scar.

Gross Examination: Specimen consists of four, fatty greyish white needle core tissue strips, longest mea
1.0cm in length; all tissue processed. (A)

Microscopy : Section shows fibroadipose breast tissue with mild mononuclear cells infiltration and
of calcifications. The tissue submitted is negative for atypia and malignancy.

Biopsy from left breast scar:

Diagnosis :- Mild chronic inflammation and calcification, negative for malignancy.
HPE no. : AG-925/22
Note :- 01 block (s) is/are dispatched with the report.

If Specimen preserved, it will be retained in the laboratory for 6 weeks from the date of receipt.

Dr.(Mrs.) Neeti S. Jainapurkar

Page 1 of 1 MBBS,MD(Path) Regn.No: G-9070
Diagnostics Pvt.

"Laboratory is accredited as per ISO 15189:2012, Certificate Number MC-3143. Scope available on request / @ www.nabl-india.org”

Carrying ftom Dr. Awanti Golwilkar
Dr. Ajit Golwilkar's Ae ain MO (Pathology)

legacy of Over BE WELL Dr. Vinanti Golwilkar
Four Decades oh srerstear mf. AG Diagnostics Pvt. Lid MD (Pathology)
"""

# Loop through the dictionary and extract values
extracted_data = {}
for key, regex in desired_values.items():
  match = re.findall(regex, text)
  if match:
    extracted_data[key] = match[0].strip()

# Print the extracted data
for key, value in extracted_data.items():
  print(f"{key}: {value}")
