
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
import DataStructures

def testCreateCostEvent(tested_event, test_payer_member): 
    if tested_event.getPayer() !=  test_payer_member:
        return False
    if tested_event.getDescription() != "":
        return False
    if tested_event.getTag() != "":
        return False
    return True

##we aint sure what's the diff between the return of Calculate Cost & ExectedCost input?
def testCalculateCost(tested_event, test_expectedCost_dict):
    if tested_event.calculateCost() != test_expectedCost_dict:
        return False
    return True

def testsetTag(tested_event, testing_tag_1, testing_tag_2):
    tested_event.setTag(testing_tag_1)
    if tested_event.getTag() != testing_tag_1:
        return False
    #testing overwrite
    tested_event.setTag(testing_tag_2)
    if tested_event.getTag() != testing_tag_2:
        return False
    return True

def testsetDescription(tested_event, testing_description):
    tested_event.setDescription(testing_description)
    if tested_event.getTag() != testing_description:
        return False
    return True

##we dont know what balancesheet and transactionsheet should look like (should prob be more of interface thing?/)
def testCreateCostManager(tested_costManager, initialized_balance_sheet_beforeaddmember,initialized_transaction_sheet):
    if tested_costManager.getBalanceSheet() == None:
        return False
    if tested_costManager.getBalanceSheet() != initialized_balance_sheet_beforeaddmember:
        return False
    if tested_costManager.getTransactionSheet() == None:
        return False
    if tested_costManager.getTransactionSheet() == initialized_transaction_sheet:
        return False
    return True

def testaddmember(tested_costManager, newMember):
    tested_costManager.addMember(newMember)
    #no getmember sadge 
    if tested_costManager.listOfMembers != after_added_members:
        return False
    return True

#incomplete because CostManager's function is not complete yet 
def testdeleteMember(tested_costManager):
    return True

#testing safety, if adding cost will change transactionsheet to null (we have no other stuff)
def testadd_delete_Cost(tested_costManager,transaction_sheet_afteraddcost):
     #testing addCost
    tested_costManager.addCost(tested_event)
    if tested_costManager.getTransactionSheet == None:
        return False
    if tested_costManager.getTransactionSheet != transaction_sheet_afteraddcost:
        return False

    #testing calculateResult: update balancesheet, 
    tested_costManager.calculateResult()
    if tested_costManager.getBalanceSheet != balance_sheet_afteraddcost:
        return False

    #testing deleteCost    
    tested_costManager.deleteCost(tested_event)
    if tested_costManager.getTransactionSheet() == initialized_transaction_sheet:
        return False
    return True


if __name__ == "__main__":
    test_payer_member = Member("Jessica", "purple")
    test_debter_1 = Member("Julia", "pink")
    test_debter_2 = Member("Esther", "blue")
    actual_cost = 120 
    test_expectedCost_dict = {
        test_debter_1: 40 ,
        test_debter_2: 40
    }

    tested_event = Cost(test_payer_member,actual_cost,test_expectedCost_dict)
    testing_tag_1 = "testing testing tag tag 1 "
    testing_tag_2 = "testing teting tag tag tag 2"
    testing_description = "This is an event description"

    list_of_members = {
        "Jessica": test_payer_member,
        "Julia": test_debter_1,
    }

    after_added_members = {
        "Jessica": test_payer_member,
        "Julia": test_debter_1,
        'Esther': test_debter_2
    }

    tested_costManager = CostManager(list_of_members)
    initialized_balance_sheet_beforeaddmember = {
        "Jessica": {
            "Jessica": 0,
            "Julia": 0,
        },
        "Julia":{
            "Jessica": 0,
            "Julia": 0,
        }
    }

    initialized_transaction_sheet = []
    transaction_sheet_afteraddcost = [tested_event]
    balance_sheet_afteraddcost = {
        "Jessica": {
            "Jessica":0,
            "Julia":40,
            "Esther":40,
        },
        "Julia":{
            "Jessica":-40,
            "Julia": 0,
            "Esther":0,
        },
        "Esther":{
            "Jessica":-40,
            "Julia":0 ,
            "Esther":0,
        },
    }

    assert (testCreateCostEvent(tested_event, test_payer_member))
    assert (testCalculateCost(tested_event))
    assert (testsetTag(tested_event,testing_tag_1,testing_tag_2))
    assert (testCreateCostManager(tested_costManager, initialized_balance_sheet_beforeaddmember))
    assert (testaddmember(tested_costManager,test_debter_2))
    assert (testadd_delete_Cost(initialized_transaction_sheet,transaction_sheet_afteraddcost, balance_sheet_afteraddcost))