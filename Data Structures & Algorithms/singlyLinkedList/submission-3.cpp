class Node {
public:
    int val;
    Node* next;

    Node(int val, Node* next) : val(val), next(next) {
    }
};

class LinkedList {
private:
    Node* head;
    Node* tail;

public:
    LinkedList() {
        head = new Node(-1, nullptr);
        tail = nullptr;
    }

    int get(int index) {
        Node* cur = head->next;
        for (int i = 0; i < index; ++i) {
            if (cur == nullptr) {
                return -1;
            }
            cur = cur->next;
        }
        if (cur == nullptr) { 
            return -1;
        } 
        return cur->val;
    }

    void insertHead(int val) {
        Node* new_node = new Node(val, head->next);
        head->next = new_node;
        if (tail == nullptr) {
            tail = new_node;
        }
    }
    
    void insertTail(int val) {
        Node* new_node = new Node(val, nullptr);
        if (tail == nullptr) {
            head->next = new_node;
        } else {
            tail->next = new_node;
        }
        tail = new_node;
    }

    bool remove(int index) {
        Node* cur = head;
        for (int i = 0; i < index; ++i) {
            if (cur == nullptr) {
                return false;
            }
            cur = cur->next;
        }
        if (cur == nullptr || cur->next == nullptr) { 
            return false;
        } 

        if (cur->next == tail) {
            cur->next = nullptr;
            delete tail;
            tail = cur;
        } else {
            Node* temp = cur->next->next;
            delete cur->next;
            cur->next = temp;
        }

        return true;
    }

    vector<int> getValues() {
        vector<int> res;
        Node* cur = head->next;
        while (cur) {
            res.push_back(cur->val);
            cur = cur->next;
        }
        return res;
    }
};
