========== CATEGORY RESULTS ==========
Accuracy: 0.19716646989374262
                       precision    recall     f1-score   support
Billing inquiry          0.18        0.13          0.15     357
Cancellation request     0.20        0.22          0.21     327
Product inquiry          0.19        0.20          0.19     316
Refund request           0.19        0.20          0.19     345
Technical issue          0.22        0.23          0.23     349
accuracy                                           0.20     1694
macro avg                0.20        0.20          0.20     1694
weighted avg             0.20        0.20          0.20     1694

========== PRIORITY RESULTS ==========
Accuracy: 0.2579693034238489
              precision      recall        f1-score     support
Critical        0.24          0.26          0.25          411
High            0.26          0.27          0.27          409
Low             0.24          0.22          0.23          415
Medium          0.29          0.28          0.28          459
accuracy                                    0.26          1694
macro avg       0.26          0.26          0.26          1694
weighted avg    0.26          0.26          0.26          1694

========== SAMPLE PREDICTIONS ==========

Input: My payment failed and money got deducted
Predicted Category: Product inquiry
Predicted Priority: Medium

Input: Unable to login to my account
Predicted Category: Technical issue
Predicted Priority: Medium

Input: I want to cancel my order
Predicted Category: Billing inquiry
Predicted Priority: Critical

Input: App is not working properly
Predicted Category: Technical issue
Predicted Priority: High

Input: Need refund for my purchase
Predicted Category: Refund request
Predicted Priority: Low
