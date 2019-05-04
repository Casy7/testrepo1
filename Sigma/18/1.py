import json

country_info = {
	"AF": {
		"name": "Afghanistan"
	},
	"AL": {
		"name": "Albania"
	},
	"DZ": {
		"name": "Algeria"
	},
	"AS": {
		"name": "American Samoa"
	},
	"AD": {
		"name": "Andorra"
	},
	"AO": {
		"name": "Angola"
	},
	"AI": {
		"name": "Anguilla"
	},
	"AQ": {
		"name": "Antarctica"
	},
	"AG": {
		"name": "Antigua & Barbuda"
	},
	"AR": {
		"name": "Argentina"
	},
	"AM": {
		"name": "Armenia"
	},
	"AW": {
		"name": "Aruba"
	},
	"AU": {
		"name": "Australia"
	},
	"AT": {
		"name": "Austria"
	},
	"AZ": {
		"name": "Azerbaijan"
	},
	"BS": {
		"name": "Bahamas"
	},
	"BH": {
		"name": "Bahrain"
	},
	"BD": {
		"name": "Bangladesh"
	},
	"BB": {
		"name": "Barbados"
	},
	"BY": {
		"name": "Belarus"
	},
	"BE": {
		"name": "Belgium"
	},
	"BZ": {
		"name": "Belize"
	},
	"BJ": {
		"name": "Benin"
	},
	"BM": {
		"name": "Bermuda"
	},
	"BT": {
		"name": "Bhutan"
	},
	"BO": {
		"name": "Bolivia"
	},
	"BA": {
		"name": "Bosnia & Herzegovina"
	},
	"BW": {
		"name": "Botswana"
	},
	"BV": {
		"name": "Bouvet Island"
	},
	"BR": {
		"name": "Brazil"
	},
	"IO": {
		"name": "British Indian Ocean Territory"
	},
	"BN": {
		"name": "Brunei Darussalam"
	},
	"BG": {
		"name": "Bulgaria"
	},
	"BF": {
		"name": "Burkina Faso"
	},
	"BI": {
		"name": "Burundi"
	},
	"KH": {
		"name": "Cambodia"
	},
	"CM": {
		"name": "Cameroon"
	},
	"CA": {
		"name": "Canada"
	},
	"CV": {
		"name": "Cape Verde"
	},
	"KY": {
		"name": "Cayman Islands"
	},
	"CF": {
		"name": "Central African Republic"
	},
	"TD": {
		"name": "Chad"
	},
	"CL": {
		"name": "Chile"
	},
	"CN": {
		"name": "China"
	},
	"CX": {
		"name": "Christmas Island"
	},
	"CC": {
		"name": "Cocos (Keeling) Islands"
	},
	"CO": {
		"name": "Colombia"
	},
	"KM": {
		"name": "Comoros"
	},
	"CG": {
		"name": "Congo"
	},
	"CD": {
		"name": "Zaire"
	},
	"CK": {
		"name": "Cook Islands"
	},
	"CR": {
		"name": "Costa Rica"
	},
	"CI": {
		"name": "Cote D'ivoire (Ivory Coast)"
	},
	"HR": {
		"name": "Croatia (Hrvatska)"
	},
	"CU": {
		"name": "Cuba"
	},
	"CY": {
		"name": "Cyprus"
	},
	"CZ": {
		"name": "Czech Republic"
	},
	"DK": {
		"name": "Denmark"
	},
	"DJ": {
		"name": "Djibouti"
	},
	"DM": {
		"name": "Dominica"
	},
	"DO": {
		"name": "Dominican Republic"
	},
	"TP": {
		"name": "East Timor"
	},
	"EC": {
		"name": "Ecuador"
	},
	"EG": {
		"name": "Egypt"
	},
	"SV": {
		"name": "El Salvador"
	},
	"GQ": {
		"name": "Equatorial Guinea"
	},
	"ER": {
		"name": "Eritrea"
	},
	"EE": {
		"name": "Estonia"
	},
	"ET": {
		"name": "Ethiopia"
	},
	"FK": {
		"name": "Falkland Islands (Malvinas)"
	},
	"FO": {
		"name": "Faroe Islands"
	},
	"FJ": {
		"name": "Fiji"
	},
	"FI": {
		"name": "Finland"
	},
	"FR": {
		"name": "France"
	},
	"GF": {
		"name": "French Guiana"
	},
	"PF": {
		"name": "French Polynesia"
	},
	"TF": {
		"name": "French Southern Territories"
	},
	"GA": {
		"name": "Gabon"
	},
	"GM": {
		"name": "Gambia"
	},
	"GE": {
		"name": "Georgia"
	},
	"DE": {
		"name": "Germany"
	},
	"GH": {
		"name": "Ghana"
	},
	"GI": {
		"name": "Gibraltar"
	},
	"GB": {
		"name": "United Kingdom"
	},
	"GR": {
		"name": "Greece"
	},
	"GL": {
		"name": "Greenland"
	},
	"GD": {
		"name": "Grenada"
	},
	"GP": {
		"name": "Guadeloupe"
	},
	"GU": {
		"name": "Guam"
	},
	"GT": {
		"name": "Guatemala"
	},
	"GN": {
		"name": "Guinea"
	},
	"GW": {
		"name": "Guinea-Bissau"
	},
	"GY": {
		"name": "Guyana"
	},
	"HT": {
		"name": "Haiti"
	},
	"HM": {
		"name": "Heard & McDonald Islands"
	},
	"VA": {
		"name": "Vatican City (Holy See)"
	},
	"HN": {
		"name": "Honduras"
	},
	"HK": {
		"name": "Hong Kong"
	},
	"HU": {
		"name": "Hungary"
	},
	"IS": {
		"name": "Iceland"
	},
	"IN": {
		"name": "India"
	},
	"ID": {
		"name": "Indonesia"
	},
	"IR": {
		"name": "Iran"
	},
	"IQ": {
		"name": "Iraq"
	},
	"IE": {
		"name": "Ireland"
	},
	"IL": {
		"name": "Israel"
	},
	"IT": {
		"name": "Italy"
	},
	"JM": {
		"name": "Jamaica"
	},
	"JP": {
		"name": "Japan"
	},
	"JO": {
		"name": "Jordan"
	},
	"KZ": {
		"name": "Kazakhstan"
	},
	"KE": {
		"name": "Kenya"
	},
	"KI": {
		"name": "Kiribati"
	},
	"KP": {
		"name": "Korea (North)"
	},
	"KR": {
		"name": "Korea (South)"
	},
	"KW": {
		"name": "Kuwait"
	},
	"KG": {
		"name": "Kyrgyzstan"
	},
	"LA": {
		"name": "Laos"
	},
	"LV": {
		"name": "Latvia"
	},
	"LB": {
		"name": "Lebanon"
	},
	"LS": {
		"name": "Lesotho"
	},
	"LR": {
		"name": "Liberia"
	},
	"LY": {
		"name": "Libya"
	},
	"LI": {
		"name": "Liechtenstein"
	},
	"LT": {
		"name": "Lithuania"
	},
	"LU": {
		"name": "Luxembourg"
	},
	"MO": {
		"name": "Macau"
	},
	"MK": {
		"name": "Macedonia"
	},
	"MG": {
		"name": "Madagascar"
	},
	"MW": {
		"name": "Malawi"
	},
	"MY": {
		"name": "Malaysia"
	},
	"MV": {
		"name": "Maldives"
	},
	"ML": {
		"name": "Mali"
	},
	"MT": {
		"name": "Malta"
	},
	"MH": {
		"name": "Marshall Islands"
	},
	"MQ": {
		"name": "Martinique"
	},
	"MR": {
		"name": "Mauritania"
	},
	"MU": {
		"name": "Mauritius"
	},
	"YT": {
		"name": "Mayotte"
	},
	"MX": {
		"name": "Mexico"
	},
	"FM": {
		"name": "Micronesia"
	},
	"MD": {
		"name": "Moldova"
	},
	"MC": {
		"name": "Monaco"
	},
	"MN": {
		"name": "Mongolia"
	},
	"MS": {
		"name": "Montserrat"
	},
	"MA": {
		"name": "Morocco"
	},
	"MZ": {
		"name": "Mozambique"
	},
	"MM": {
		"name": "Myanmar"
	},
	"NA": {
		"name": "Namibia"
	},
	"NR": {
		"name": "Nauru"
	},
	"NP": {
		"name": "Nepal"
	},
	"NL": {
		"name": "Netherlands"
	},
	"AN": {
		"name": "Netherlands Antilles"
	},
	"NC": {
		"name": "New Caledonia"
	},
	"NZ": {
		"name": "New Zealand"
	},
	"NI": {
		"name": "Nicaragua"
	},
	"NE": {
		"name": "Niger"
	},
	"NG": {
		"name": "Nigeria"
	},
	"NU": {
		"name": "Niue"
	},
	"NF": {
		"name": "Norfolk Island"
	},
	"MP": {
		"name": "Northern Mariana Islands"
	},
	"NO": {
		"name": "Norway"
	},
	"OM": {
		"name": "Oman"
	},
	"PK": {
		"name": "Pakistan"
	},
	"PW": {
		"name": "Palau"
	},
	"PA": {
		"name": "Panama"
	},
	"PG": {
		"name": "Papua New Guinea"
	},
	"PY": {
		"name": "Paraguay"
	},
	"PE": {
		"name": "Peru"
	},
	"PH": {
		"name": "Philippines"
	},
	"PN": {
		"name": "Pitcairn"
	},
	"PL": {
		"name": "Poland"
	},
	"PT": {
		"name": "Portugal"
	},
	"PR": {
		"name": "Puerto Rico"
	},
	"QA": {
		"name": "Qatar"
	},
	"RE": {
		"name": "Reunion"
	},
	"RO": {
		"name": "Romania"
	},
	"RU": {
		"name": "Russian Federation"
	},
	"RW": {
		"name": "Rwanda"
	},
	"SH": {
		"name": "St. Helena"
	},
	"KN": {
		"name": "Saint Kitts & Nevis"
	},
	"LC": {
		"name": "Saint Lucia"
	},
	"PM": {
		"name": "St. Pierre & Miquelon"
	},
	"VC": {
		"name": "St. Vincent & the Grenadines"
	},
	"WS": {
		"name": "Samoa"
	},
	"SM": {
		"name": "San Marino"
	},
	"ST": {
		"name": "Sao Tome & Principe"
	},
	"SA": {
		"name": "Saudi Arabia"
	},
	"SN": {
		"name": "Senegal"
	},
	"SC": {
		"name": "Seychelles"
	},
	"SL": {
		"name": "Sierra Leone"
	},
	"SG": {
		"name": "Singapore"
	},
	"SK": {
		"name": "Slovak Republic"
	},
	"SI": {
		"name": "Slovenia"
	},
	"SB": {
		"name": "Solomon Islands"
	},
	"SO": {
		"name": "Somalia"
	},
	"ZA": {
		"name": "South Africa"
	},
	"GS": {
		"name": "S.Georgia & S.Sandwich Islands"
	},
	"ES": {
		"name": "Spain"
	},
	"LK": {
		"name": "Sri Lanka"
	},
	"SD": {
		"name": "Sudan"
	},
	"SR": {
		"name": "Suriname"
	},
	"SJ": {
		"name": "Svalbard & Jan Mayen Islands"
	},
	"SZ": {
		"name": "Swaziland"
	},
	"SE": {
		"name": "Sweden"
	},
	"CH": {
		"name": "Switzerland"
	},
	"SY": {
		"name": "Syria"
	},
	"TW": {
		"name": "Taiwan"
	},
	"TJ": {
		"name": "Tajikistan"
	},
	"TZ": {
		"name": "Tanzania"
	},
	"TH": {
		"name": "Thailand"
	},
	"TG": {
		"name": "Togo"
	},
	"TK": {
		"name": "Tokelau"
	},
	"TO": {
		"name": "Tonga"
	},
	"TT": {
		"name": "Trinidad & Tobago"
	},
	"TN": {
		"name": "Tunisia"
	},
	"TR": {
		"name": "Turkey"
	},
	"TM": {
		"name": "Turkmenistan"
	},
	"TC": {
		"name": "Turks & Caicos Islands"
	},
	"TV": {
		"name": "Tuvalu"
	},
	"UG": {
		"name": "Uganda"
	},
	"UA": {
		"name": "Ukraine"
	},
	"AE": {
		"name": "United Arab Emirates"
	},
	"US": {
		"name": "United States"
	},
	"UY": {
		"name": "Uruguay"
	},
	"UZ": {
		"name": "Uzbekistan"
	},
	"VU": {
		"name": "Vanuatu"
	},
	"VE": {
		"name": "Venezuela"
	},
	"VN": {
		"name": "Viet Nam"
	},
	"VG": {
		"name": "Virgin Islands (British)"
	},
	"VI": {
		"name": "Virgin Islands (U.S.)"
	},
	"WF": {
		"name": "Wallis & Futuna Islands"
	},
	"EH": {
		"name": "Western Sahara"
	},
	"YE": {
		"name": "Yemen"
	},
	"YU": {
		"name": "Yugoslavia"
	},
	"ZM": {
		"name": "Zambia"
	},
	"ZW": {
		"name": "Zimbabwe"
	}
}

h = {}

for i in country_info.keys():
    h[i] = country_info[i]["name"]

with open("‪country_codes.json", "w") as write_file:
    json.dump(h, write_file)
