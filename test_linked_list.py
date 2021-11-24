from linked_list import LinkedList, Node
import pytest

def test_get_element():
    
    linked_list = LinkedList()

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'


    #HEAD -> C -> B -> A 


def test_get_element_index_too_large():
    
    linked_list = LinkedList()

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    with pytest.raises(Exception, match='index too large'):
        linked_list.get_element(3)

    with pytest.raises(Exception, match='index too large'):
        linked_list.get_element(10)

def test_count():

    linked_list = LinkedList()

    assert linked_list.count() == 0

    linked_list.push_front('a')

    assert linked_list.count() == 1

    linked_list.push_front('b')

    assert linked_list.count() == 2

    linked_list.push_front('c')

    assert linked_list.count() == 3


def test_pop_front():
    
    linked_list = LinkedList()

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'

    

    assert linked_list.pop_front() == 'c'

    #assert linked_list.get_element(0) == 'b'