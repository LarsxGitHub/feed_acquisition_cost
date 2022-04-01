# feed_acquisition_cost

It is (nigh-on) impossible to peer with certain ASes. AS721 (U.S. Department of Defense) and AS4134 (China Telecom) frequently appear as potentially beneficial peers, yet their security, privacy, and communication policies impede connecting them. In contrast, peering sessions with, e.g., personal-use ASNs can often be established within hours of first contact. 

The position of an AS along this complexity dimension depends on various aspects such as time to first contact, operational willingness to peer, or legal peering requirements. While dedicated peering coordinators may manually explore those aspects for certain ASes, scaling this approach to our needs is infeasible. Hence, we estimate this peering complexity using related features. 

We use ASDB to bootstrap our feature list. ASDB combines a multitude of databases and machine learning classifiers to associate a set of labels (e.g., "ISP", "Research and Education", or "Government and Public Administration") that characterize each AS. The latest version (from 25th Nov. 2022) describes more than 100K ASes using between 1 and 28 (out of 86 total) labels. We further extend ASDB's labels using the following databases:

* We add "state-owned" to ASes based on the public list published by Carisimo et al. [cite]
* We add "REN" to ASes based on a list of global Research and Education Networks that we received from RIPE. 
* We add "Isolario feed" to ASes that previously feed the route collector project Isolario [cite], which terminated on 31st Dec. 2021. 
* We add "personal-use" to ASes based on a public, well-maintained list of personal-use ASN [cite].
* The 2020 Open Data Inventory report published by Open Data Watch asses countries based on their coverage and openness of social, economic, and environmental databases [cite]. We use the report's available system to map the openness values (0-100%) to seven categories that we label as "ODIN-<1..7>." Afterwards, we use RIR delegation data to map each ASN to a legislative country and subsequential ODIN category (via the country code). Please note: While its infrastructure footprint may span multiple countries, an AS' data-sharing policies usually align closest with those of its organization's juridical country. 

Given the extended list of labels, we asked RIPE's peering coordinators to judge, based on their prior experiences, how much each label may influence peering complexity on an Integer scale from 3 (prevents peering) to -3 (guarantees peering). After mapping all labels to the resulting complexity modifiers, we collapse the list of modifiers for each AS as follows: 
1) If an AS has a -3 modifier, its peering complexity is 0. 
2) If an AS has a +3 modifier, its peering complexity is 1.
3) We calculate the normalized mean across an AS' modifiers. 
