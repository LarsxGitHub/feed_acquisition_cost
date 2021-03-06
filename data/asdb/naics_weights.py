NAICS_WEIGHTS = {
    'Computer and Information Technology -> Internet Service Provider (ISP)':                                                                          1,
    'Computer and Information Technology -> Phone Provider':                                                                                           0,
    'Computer and Information Technology -> "Hosting, Cloud Provider, Data Center, Server Colocation"':                                                1,
    'Computer and Information Technology -> Computer and Network Security':                                                                            0,
    'Computer and Information Technology -> Software Development':                                                                                     0,
    'Computer and Information Technology -> Technology Consulting Services':                                                                           0,
    'Computer and Information Technology -> Satellite Communication':                                                                                  0,
    'Computer and Information Technology -> Search':                                                                                                   0,
    'Computer and Information Technology -> Internet Exchange Point (IXP)':                                                                            2,
    'Computer and Information Technology -> Other':                                                                                                    0,
    '"Media, Publishing, and Broadcasting" -> Online Music and Video Streaming Services':                                                              0,
    '"Media, Publishing, and Broadcasting" -> Online Informational Content':                                                                           0,
    '"Media, Publishing, and Broadcasting" -> "Print Media (Newspapers, Magazines, Books)"':                                                           0,
    '"Media, Publishing, and Broadcasting" -> Music and Video Industry':                                                                               0,
    '"Media, Publishing, and Broadcasting" -> Radio and Television Providers':                                                                         0,
    '"Media, Publishing, and Broadcasting" -> Other':                                                                                                  0,
    'Finance and Insurance -> "Banks, Credit Card Companies, Mortgage Providers"':                                                                     0,
    'Finance and Insurance -> Insurance Carriers and Agencies':                                                                                        0,
    'Finance and Insurance -> "Accountants, Tax Preparers, Payroll Services"':                                                                         0,
    'Finance and Insurance -> "Investment, Portfolio Management, Pensions and Funds"':                                                                 0,
    'Finance and Insurance -> Other':                                                                                                                  0,
    'Education and Research -> Elementary and Secondary Schools':                                                                                      1,
    'Education and Research -> "Colleges, Universities, and Professional Schools"':                                                                    1,
    'Education and Research -> "Other Schools, Instruction, and Exam Preparation (Trade Schools, Art Schools, Driving Instruction, etc.)"':            1,
    'Education and Research -> Research and Development Organizations':                                                                                1,
    'Education and Research -> Education Software':                                                                                                    0,
    'Education and Research -> Other':                                                                                                                 0,
    'Service -> "Law, Business, and Consulting Services"':                                                                                            -1,
    'Service -> "Buildings, Repair, Maintenance (Pest Control, Landscaping, Cleaning, Locksmiths, Car Washes, etc)"':                                  0,
    'Service -> "Personal Care and Lifestyle (Barber Shops, Nail Salons, Diet Centers, Laundry, etc)"':                                                0,
    'Service -> "Social Assistance (Temporary Shelters, Emergency Relief, Child Day Care, etc)"':                                                      0,
    'Service -> Other':                                                                                                                                0,
    'Community Groups and Nonprofits -> Churches and Religious Organizations':                                                                         0,
    'Community Groups and Nonprofits -> "Human Rights and Social Advocacy (Human Rights, Environment and Wildlife Conservation, Other)"':              1,
    'Community Groups and Nonprofits -> Other':                                                                                                        0,
    'Construction and Real Estate -> Buildings (Residential or Commercial)':                                                                           0,
    'Construction and Real Estate -> "Civil Engineering Construction (Utility Lines, Roads and Bridges)"':                                             0,
    'Construction and Real Estate -> Real Estate (Residential and/or Commercial)':                                                                     0,
    'Construction and Real Estate -> Other':                                                                                                           0,
    '"Museums, Libraries, and Entertainment" -> Libraries and Archives':                                                                               0,
    '"Museums, Libraries, and Entertainment" -> "Recreation, Sports, and Performing Arts"':                                                            0,
    '"Museums, Libraries, and Entertainment" -> "Museums, Historical Sites, Zoos, Nature Parks"':                                                      0,
    '"Museums, Libraries, and Entertainment" -> Casinos and Gambling':                                                                                 0,
    '"Museums, Libraries, and Entertainment" -> Tours and Sightseeing':                                                                                0,
    '"Museums, Libraries, and Entertainment" -> Other':                                                                                                0,
    'Utilities (Excluding Internet Service) -> "Electric Power Generation, Transmission, Distribution"':                                               0,
    'Utilities (Excluding Internet Service) -> Natural Gas Distribution':                                                                              0,
    'Utilities (Excluding Internet Service) -> Water Supply and Irrigation':                                                                           0,
    'Utilities (Excluding Internet Service) -> Sewage Treatment':                                                                                      0,
    'Utilities (Excluding Internet Service) -> Steam and Air-Conditioning Supply':                                                                     0,
    'Utilities (Excluding Internet Service) -> Other':                                                                                                 0,
    'Health Care Services -> Hospitals and Medical Centers':                                                                                           0,
    'Health Care Services -> Medical Laboratories and Diagnostic Centers':                                                                             0,
    'Health Care Services -> "Nursing, Residential Care Facilities, Assisted Living, and Home Health Care"':                                           0,
    'Health Care Services -> Other':                                                                                                                   0,
    'Travel and Accommodation -> Air Travel':                                                                                                          0,
    'Travel and Accommodation -> Railroad Travel':                                                                                                     0,
    'Travel and Accommodation -> Water Travel':                                                                                                        0,
    'Travel and Accommodation -> "Hotels, Motels, Inns, Other Traveler Accommodation"':                                                                0,
    'Travel and Accommodation -> Recreational Vehicle Parks and Campgrounds':                                                                          0,
    'Travel and Accommodation -> "Boarding Houses, Dormitories, Workers??? Camps"':                                                                      0,
    'Travel and Accommodation -> Food Services and Drinking Places':                                                                                   0,
    'Travel and Accommodation -> Other':                                                                                                               0,
    '"Freight, Shipment, and Postal Services" -> Postal Services and Couriers':                                                                        0,
    '"Freight, Shipment, and Postal Services" -> Air Transportation':                                                                                  0,
    '"Freight, Shipment, and Postal Services" -> Railroad Transportation':                                                                             0,
    '"Freight, Shipment, and Postal Services" -> Water Transportation':                                                                                0,
    '"Freight, Shipment, and Postal Services" -> Trucking':                                                                                            0,
    '"Freight, Shipment, and Postal Services" -> "Space, Satellites"':                                                                                 0,
    '"Freight, Shipment, and Postal Services" -> "Passenger Transit (Car, Bus, Taxi, Subway)"':                                                        0,
    '"Freight, Shipment, and Postal Services" -> Other':                                                                                               0,
    'Government and Public Administration -> "Military, Defense, National Security, and International Affairs"':                                      -2,
    'Government and Public Administration -> "Law Enforcement, Public Safety, and Justice"':                                                          -1,
    'Government and Public Administration -> "Government and Regulatory Agencies, Administrations, Departments, and Services"':                       -1,
    '"Retail Stores, Wholesale, and E-commerce Sites" -> "Food, Grocery, Beverages"':                                                                  0,
    '"Retail Stores, Wholesale, and E-commerce Sites" -> "Clothing, Fashion, Luggage"':                                                                0,
    '"Retail Stores, Wholesale, and E-commerce Sites" -> Other':                                                                                       0,
    'Manufacturing -> Automotive and Transportation':                                                                                                  0,
    'Manufacturing -> "Food, Beverage, and Tobacco"':                                                                                                  0,
    'Manufacturing -> Clothing and Textiles':                                                                                                          0,
    'Manufacturing -> Machinery':                                                                                                                      0,
    'Manufacturing -> Chemical and Pharmaceutical Manufacturing':                                                                                      0,
    'Manufacturing -> Electronics and Computer Components':                                                                                            0,
    'Manufacturing -> Other':                                                                                                                          0,
    'Other -> Individually Owned':                                                                                                                     0,
    'Unknown -> Unknown':                                                                                                                              0
}
