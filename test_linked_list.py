from linked_list import LinkedList
import pytest


def test_get_element():
    
    linked_list = LinkedList()

    with pytest.raises(Exception, match='Linked list is empty'):
        linked_list.get_element(0)

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'


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

    assert linked_list.pop_front() == None

    linked_list.push_front('a')

    assert linked_list.pop_front() == 'a'
    
    with pytest.raises(Exception, match='Linked list is empty'):
        linked_list.get_element(0)

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'

    assert linked_list.pop_front() == 'c'
    assert linked_list.get_element(0) == 'b'
    assert linked_list.get_element(1) == 'a'


def test_insert_after():
    
    linked_list = LinkedList()

    with pytest.raises(Exception, match='Linked list is empty'):
        linked_list.insert_after(0, 'f')

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'

    # HEAD -> C -> B -> A

    linked_list.insert_after(1, 'f')

    # HEAD -> C -> B -> F -> A

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'f'
    assert linked_list.get_element(3) == 'a'

    linked_list_2 = LinkedList()

    linked_list_2.push_front('a')

    linked_list_2.insert_after(0, 'b')

    # HEAD -> A -> B

    assert linked_list_2.get_element(0) == 'a'
    assert linked_list_2.get_element(1) == 'b'
    
    linked_list_2.insert_after(1, 'c')

    assert linked_list_2.get_element(0) == 'a'
    assert linked_list_2.get_element(1) == 'b'
    assert linked_list_2.get_element(2) == 'c'


def test_remove_element():

    linked_list = LinkedList()

    with pytest.raises(Exception, match='Linked list is empty'):
        linked_list.remove_element(1)

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    linked_list.push_front('d')
    linked_list.push_front('e')

    # HEAD -> E -> D -> C -> B -> A

    assert linked_list.get_element(0) == 'e'
    assert linked_list.get_element(1) == 'd'
    assert linked_list.get_element(2) == 'c'
    assert linked_list.get_element(3) == 'b'
    assert linked_list.get_element(4) == 'a'

    #REMOVING ELEMENT IN THE MIDDLE OF THE LIST
    assert linked_list.remove_element(1) == 'd'

    # HEAD -> E -> C -> B -> A

    assert linked_list.get_element(0) == 'e'
    assert linked_list.get_element(1) == 'c'
    assert linked_list.get_element(2) == 'b'
    assert linked_list.get_element(3) == 'a'

    
    #REMOVING ELEMENT AT THE BEGGINING OF THE LIST
    assert linked_list.remove_element(0) == 'e'

    # HEAD -> C -> B -> A

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'
    assert linked_list.get_element(2) == 'a'

    
    #REMOVING ELEMENT AT THE END OF THE LIST
    assert linked_list.remove_element(2) == 'a'

    # HEAD -> C -> B

    assert linked_list.get_element(0) == 'c'
    assert linked_list.get_element(1) == 'b'


def test_reverse():

    linked_list = LinkedList()

    with pytest.raises(Exception, match='Linked list is empty'):
        linked_list.remove_element(1)

    linked_list.push_front('a')
    linked_list.push_front('b')
    linked_list.push_front('c')
    linked_list.push_front('d')
    linked_list.push_front('e')

    assert linked_list.get_element(0) == 'e'
    assert linked_list.get_element(1) == 'd'
    assert linked_list.get_element(2) == 'c'
    assert linked_list.get_element(3) == 'b'
    assert linked_list.get_element(4) == 'a'

    # HEAD -> E -> D -> C -> B -> A

    linked_list.reverse()

    #assert linked_list.get_element(0) == 'e'
    #assert linked_list.get_element(1) == 'e'
    #assert linked_list.get_element(2) == 'e'
    #assert linked_list.get_element(3) == 'e'
    #assert linked_list.get_element(4) == 'e'

    #assert linked_list.get_element(0) == 'a'
    #assert linked_list.get_element(1) == 'b'
    #assert linked_list.get_element(2) == 'c'
    #assert linked_list.get_element(3) == 'd'
    #assert linked_list.get_element(4) == 'e'

    # HEAD -> A -> B -> C -> D -> E