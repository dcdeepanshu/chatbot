import logging
import json
import csv

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted,ConversationPaused,FollowupAction
from typing import Text, Dict, Any, List
from rasa_core_sdk.executor import CollectingDispatcher


logger = logging.getLogger(__name__)

#class ActionGreet(Action):

#	def name(self):
#		return "action_greet"		
#	def run(self, dispatcher, tracker, domain):
#		intent = tracker.latest_message['intent'].get('name')
#			dispatcher.utter_template("utter_greet", tracker)
#			return []
#		else:
#			dispatcher.utter_template("utter_vidalbot", tracker)
#			dispatcher.utter_template("utter_menuortext", tracker)
#			return []
		
class ActionFaqs(Action):

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
		
		# get the latest intent and append 'utter_' before the intent to send the answer to the user
		
        if intent in ['menu','view_appointment','network_hosp','cashless_status','reimbursement_status','login','mobile_email','otp','set_password','reset_password','login_issue','greet','goodbye','ask_howdoing','ask_isbot','appointment','Doctor_Search','Hospital_Search','search_specialty','online_consult','E_card','Enrollment','Policy_details','health',
		'out_of_scope','cashless_procedure',' cancel_cashless','affirm','ask_whatspossible','something_else','time_preauth','pay_cashless','non_medical_expenses','timelimit_hospital','cashless_rejection','ask_daycaresurgeries','claim_rejection','ask_disallowed_amount','shortfall','docu_reimbursement','reimbursement_procedure','planned_hospitalisation','ask_appoint_confirm','ask_emergency_hospitalisation','ask_invoice','make_pay','pay_issue','thankyou','handleinsult','nicetomeeyou','ask_languagesbot','ask_howold','ask_wherefrom','ask_whoisit','ask_builder','ask_claim_shortfall','ask_claim_status','when_submit_claim']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []

class ActionDefaultAskAffirmation(Action):

    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self):
        return 'action_default_ask_affirmation'

    def __init__(self):
        self.intent_mappings = {}

       # read the mapping from a csv and store it in a dictionary

        with open('data/intent_mapping.csv', newline='',
                  encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.intent_mappings[row[0]] = row[1]

    def run(
        self,
        dispatcher,
        tracker,
        domain,
        ):

       # get the most likely intent i.e latest intent from the tracker

        last_intent_name = tracker.latest_message['intent'].get('name')

       # get the prompt for the intent i.e matches the intent name with the description from the csv file

        intent_prompt = self.intent_mappings[last_intent_name]

       # Create the message with two buttons to it to ask user if he means the latest intent in the tracker
      
        message = "Sorry, I'm not sure I've understood you correctly. Do you mean..."
        buttons = []
        buttons.append({'title': '{}'.format(intent_prompt),
                       'payload': '/{}'.format(last_intent_name)})
        buttons.append({'title': 'Something else',
                       'payload': '/something_else'})
        dispatcher.utter_button_message(message, buttons=buttons)

        return []
		
class ActionDefaultFallback(Action):
		
	def name(self) -> Text:
		return "action_default_fallback"

	def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List['Event']:

    # Fallback caused by TwoStageFallbackPolicy
		if (len(tracker.events) >= 4 and tracker.events[-4].get('name') =='action_default_ask_affirmation'):

			dispatcher.utter_template('utter_ask_rephrase', tracker)

			return []

    # Fallback caused by Core
		else:
			dispatcher.utter_template('utter_default', tracker)
			return [UserUtteranceReverted()]