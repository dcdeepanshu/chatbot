##story 001
* greet
	- utter_vidalbot
* menu
	- utter_menu
* appointment
	- utter_appointment
* Doctor_Search
	- utter_Doctor_Search
* search_specialty
	- utter_search_specialty
* goodbye
	- utter_goodbye
	- action_restart

##story 002
* greet
	- utter_vidalbot
* menu
	- utter_menu
* appointment
	- utter_appointment
* Hospital_Search
	- utter_Hospital_Search
* goodbye
	- utter_goodbye
	- action_restart

##story 003
* greet
	- utter_vidalbot
* menu
	- utter_menu
* online_consult
	- utter_online_consult
* goodbye
	- utter_goodbye
	- action_restart

##story 004
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* Policy_details
	- utter_Policy_details
* goodbye
	- utter_goodbye
	- action_restart
	

##story 005
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* E_card
	- utter_E_card
* goodbye
	- utter_goodbye
	- action_restart
	
##story 006
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* Enrollment
	- utter_Enrollment
* goodbye
	- utter_goodbye
	- action_restart
	
##story 001
* greet
	- utter_vidalbot
* menu
	- utter_menu
* appointment
	- utter_appointment
* Doctor_Search
	- utter_Doctor_Search
* search_specialty
	- utter_search_specialty
* menu
	- utter_menu
* appointment
	- utter_appointment
* Hospital_Search
	- utter_Hospital_Search
* goodbye
	- utter_goodbye
	- action_restart

##story 002
* greet
	- utter_vidalbot
* menu
	- utter_menu
* appointment
	- utter_appointment
* Hospital_Search
	- utter_Hospital_Search
* menu
	- utter_menu
* appointment
	- utter_appointment
* Doctor_Search
	- utter_Doctor_Search
* goodbye
	- utter_goodbye
	- action_restart

##story 003
* greet
	- utter_vidalbot
* menu
	- utter_menu
* online_consult
	- utter_online_consult
* menu
	- utter_menu
* appointment
	- utter_appointment
* Hospital_Search
	- utter_Hospital_Search
* goodbye
	- utter_goodbye
	- action_restart

##story 004
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* Policy_details
	- utter_Policy_details
* menu
	- utter_menu
* health
	- utter_health
* E_card
	- utter_E_card
* goodbye
	- utter_goodbye
	- action_restart
	

##story 005
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* E_card
	- utter_E_card
* goodbye
	- utter_goodbye
	- action_restart
	
##story 006
* greet
	- utter_vidalbot
* menu
	- utter_menu
* health
	- utter_health
* Enrollment
	- utter_Enrollment
* goodbye
	- utter_goodbye
	- action_restart
	
##story 1
* greet
	- utter_vidalbot
* ask_howdoing 
	- utter_ask_howdoing
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR ask_whatspossible   
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart
	

##story 2
* greet
	- utter_vidalbot
* ask_howdoing 
	- utter_ask_howdoing
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR ask_whatspossible 
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim     
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm OR ask_whatspossible
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart

##story 3
* greet
	- utter_vidalbot
* ask_howdoing 
	- utter_ask_howdoing
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR ask_whatspossible     
	- action_faqs
* network_hosp OR reimbursement_status OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm 
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm 
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim     
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart
	
##story 4
* greet
	- utter_vidalbot
* login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim 
	- action_faqs
* network_hosp OR reimbursement_status OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm OR ask_whatspossible   
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm    
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim    
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart
	
##story 5
* greet
	- utter_vidalbot
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR ask_whatspossible     
	- action_faqs
* network_hosp OR reimbursement_status OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim  
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim OR affirm    
	- action_faqs
* network_hosp OR reimbursement_status OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim     
	- action_faqs
* login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim  
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart

##faq2
* greet
	- utter_vidalbot
* network_hosp OR reimbursement_status OR view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue OR affirm
	- action_faqs
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue
	- action_faqs
* view_appointment OR  login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim     
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart
	
##faq3
* greet
	- utter_vidalbot
*  cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* network_hosp OR reimbursement_status OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue OR affirm
	- action_faqs
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue OR ask_whatspossible
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* goodbye
	- utter_goodbye
	- action_restart
	
##faq4
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue
	- action_faqs
* view_appointment OR login OR mobile_email OR otp OR set_password OR reset_password OR login_issue OR menu OR ask_isbot OR appointment OR Doctor_Search OR  Hospital_Search OR search_specialty OR online_consult OR E_card OR Enrollment OR Policy_details OR health OR out_of_scope OR thankyou OR handleinsult OR nicetomeeyou OR ask_languagesbot OR ask_howold OR ask_wherefrom OR ask_whoisit OR ask_builder OR ask_claim_shortfall OR ask_claim_status OR when_submit_claim   
	- action_faqs
* network_hosp OR reimbursement_status OR cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue OR affirm OR ask_whatspossible
	- action_faqs
* cashless_status OR cashless_procedure OR cancel_cashless OR time_preauth OR pay_cashless OR non_medical_expenses OR timelimit_hospital OR cashless_rejection OR ask_daycaresurgeries OR claim_rejection OR ask_disallowed_amount OR shortfall OR docu_reimbursement OR reimbursement_procedure OR planned_hospitalisation OR ask_emergency_hospitalisation OR ask_invoice OR make_pay OR pay_issue
	- action_faqs























