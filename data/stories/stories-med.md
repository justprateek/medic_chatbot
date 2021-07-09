## greet_reply
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2



## appointment_only
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality":"radiologist"}
  - slot{"speciality": "radiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name":"Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date":"24","month":"jan"}
  - slot{"date": "24"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time":"10:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "radiologist"}
  - slot{"speciality": "radiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Ray"}
  - slot{"doctor_name": "Ray"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "24", "month": "jan"}
  - slot{"date": "24"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "11:00"}
  - slot{"time": "11:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "radiologist"}
  - slot{"speciality": "radiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "23", "month": "jan"}
  - slot{"date": "23"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "10:00"}
  - slot{"time": "10:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "cardiologist"}
  - slot{"speciality": "cardiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "25", "month": "january"}
  - slot{"date": "25"}
  - slot{"month": "january"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "3:00"}
  - slot{"time": "3:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "dermatologist"}
  - slot{"speciality": "dermatologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Ray"}
  - slot{"doctor_name": "Ray"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "25", "month": "feb"}
  - slot{"date": "25"}
  - slot{"month": "feb"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "2:00"}
  - slot{"time": "2:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "cardiologist"}
  - slot{"speciality": "cardiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "24", "month": "February"}
  - slot{"date": "24"}
  - slot{"month": "February"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "3pm"}
  - slot{"time": "3pm"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## booking_story
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "cardiologist"}
  - slot{"speciality": "cardiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "24", "month": "February"}
  - slot{"date": "24"}
  - slot{"month": "February"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "3pm"}
  - slot{"time": "3pm"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details




## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "radiologist"}
  - slot{"speciality": "radiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "24", "month": "jan"}
  - slot{"date": "24"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "11:00"}
  - slot{"time": "11:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "radiologist"}
  - slot{"speciality": "radiologist"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Gupta"}
  - slot{"doctor_name": "Gupta"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "24", "month": "jan"}
  - slot{"date": "24"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "11:00"}
  - slot{"time": "11:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details






## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_booking_0_2
  - utter_ask_doctor_speciality_0_3
* get_speciality_0_3{"speciality": "General Practitioner"}
  - slot{"speciality": "General Practitioner"}
  - utter_ask_doctor_name_0_4
* get_doctor_name_0_4{"doctor_name": "Bora"}
  - slot{"doctor_name": "Bora"}
  - utter_ask_date_and_month_0_5
* get_date_and_month_0_5{"date": "30", "month": "jan"}
  - slot{"date": "30"}
  - slot{"month": "jan"}
  - utter_ask_time_0_6
* get_time_0_6{"time": "10:00"}
  - slot{"time": "10:00"}
  - utter_final_booking_0_7
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## interactive_story_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## no
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## select_question
* select_question_0_8
  - utter_continue_with_question_0_10
  - action_save_conversation
  - utter_saved_details



## random
* random_0_9
  - utter_cannot_understand_0_11
  - action_save_conversation
  - utter_saved_details



## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details




## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c 
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details
  






## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## health_related
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details



## cold
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - action_save_conversation
  - utter_saved_details



## cold
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cold_1_5_1
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details

## cold
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details


## cold
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8
  - action_save_conversation
  - utter_saved_details

## cold
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8







## cough
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15



## cough
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cough_1_5_2
  - utter_any_other_question_0_8


## cough
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8


## cough
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8


## cough
* problem_cough_or_cold_1_5
   - utter_ask_report_0_16
* no_report 
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8



## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3
  - utter_any_other_question_0_8




## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c 
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8


## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8


## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_3c
  - utter_any_other_question_0_8
  






## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4
  - utter_any_other_question_0_8


## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8


## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8


## health_related
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_headache_1_4_4c
  - utter_any_other_question_0_8



## cold
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15



## cold
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cold_1_5_1
  - utter_any_other_question_0_8

## cold
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8


## cold
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8

## cold
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_nasal_1_5_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cold_1_5_1c
  - utter_any_other_question_0_8







## cough
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15



## cough
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cough_1_5_2
  - utter_any_other_question_0_8


## cough
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8


## cough
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8


## cough
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_cough_1_5_2c
  - utter_any_other_question_0_8



## fever
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_ask_nasal_1_5_1
* problem_not_nasal_1_5_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15











## fungal
* problem_fungal_1_6
   - utter_ask_report_0_16
* no_report 
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15



## fungal
* problem_fungal_1_6
   - utter_ask_report_0_16
* no_report 
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_fungal_1_6
  - utter_any_other_question_0_8


## fungal
* problem_fungal_1_6
   - utter_ask_report_0_16
* no_report 
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_fungal_1_6c
  - utter_any_other_question_0_8


## fungal
* problem_fungal_1_6
   - utter_ask_report_0_16
* no_report 
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_fungal_1_6c
  - utter_any_other_question_0_8


## fungal
* problem_fungal_1_6
   - utter_ask_report_0_16
* no_report 
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_fungal_1_6c
  - utter_any_other_question_0_8





## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_diarrhea_1_7_1
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15

## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_not_diarrhea_1_7_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15




## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_diarrhea_1_7_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_diarrhea_1_7
  - utter_any_other_question_0_8


## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_diarrhea_1_7_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_diarrhea_1_7c
  - utter_any_other_question_0_8


## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_diarrhea_1_7_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_diarrhea_1_7c
  - utter_any_other_question_0_8


## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_diarrhea_1_7_1
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_diarrhea_1_7c
  - utter_any_other_question_0_8






## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_not_diarrhea_1_7_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_loose_motion_1_8
  - utter_any_other_question_0_8


## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_not_diarrhea_1_7_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_loose_motion_1_8c
  - utter_any_other_question_0_8

## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_not_diarrhea_1_7_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_loose_motion_1_8c
  - utter_any_other_question_0_8


## stomach
* problem_stomach_1_7
   - utter_ask_report_0_16
* no_report 
  - utter_ask_diarrhea_1_7_1
* problem_not_diarrhea_1_7_2
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_loose_motion_1_8c
  - utter_any_other_question_0_8



## long_duration_fever
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_1
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1 OR problem_headache_1_4_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15


## long_duration_fever
* problem_fever_1_8
   - utter_ask_report_0_16
* no_report 
  - utter_ask_headache_1_9
* problem_headache_1_9_2
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1 OR problem_headache_1_4_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15

## long duration
* problem_headache_1_4
   - utter_ask_report_0_16
* no_report 
  - utter_headache_1_4_1
  - utter_headache_1_4_2
* problem_headache_1_4_1 OR problem_headache_1_4_2
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15



## hospital
* problem_hospital_0_14
  - utter_hospital_0_15



## conjunctivitis_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_conjunctivitis_1_b
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_conjunctivitis_1_b
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_3
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_conjunctivitis_1_a
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_4
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_conjunctivitis_1_a
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## conjunctivitis_5
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## conjunctivitis_1_1
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_conjunctivitis_1_b
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_2_1
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_conjunctivitis_1_b
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_3_1
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_conjunctivitis_1_a
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## conjunctivitis_4_1
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_conjunctivitis_1_a
  - utter_conjunctivitis_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## conjunctivitis_5_1
* problem_conjunctivitis
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

<!-- k-v-n-p -->

## acne_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_acne_1_b
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## acne_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_acne_1_b
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## acne_3
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_acne_1_a
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## acne_4
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_acne_1_a
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## acne_5
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## acne_1_1
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_acne_1_b
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## acne_2_1
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_acne_1_b
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## acne_3_1
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_acne_1_a
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## acne_4_1
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_acne_1_a
  - utter_acne_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## acne_5_1
* problem_acne
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## depression_1
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_depression_1_b
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_2
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_depression_1_b
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_3
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_depression_1_a
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_4
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_depression_1_a
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## depression_5
* greet_0_1
  - utter_welcome_0_1
  - utter_ask_booking_or_question_0_2
* select_question_0_8
  - utter_continue_with_question_0_10
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details


## depression_1_1
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11
  - utter_depression_1_b
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_2_1
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_depression_1_b
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_3_1
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11
  - utter_depression_1_a
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details

## depression_4_1
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* small_duration_0_12
  - utter_ask_age_0_12
* age_0_10c
  - utter_ask_weight_0_13
* weight_0_11c
  - utter_depression_1_a
  - utter_depression_advice
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details



## depression_5_1
* problem_depression
  - utter_ask_report_0_16
* no_report
  - utter_ask_duration_0_14
* long_duration_0_13
  - utter_hospital_0_15
  - utter_any_other_question_0_8
* get_no_0_7
  - utter_have_a_good_day_0_9
  - action_save_conversation
  - utter_saved_details









