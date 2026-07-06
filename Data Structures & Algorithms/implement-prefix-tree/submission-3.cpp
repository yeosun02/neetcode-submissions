class Node {
public:
    bool is_word = false;
    unordered_map<char, Node*> children;
};

class PrefixTree {
private:
    Node* words;

public:
    PrefixTree() {
        words = new Node();
    }
    
    void insert(string word) {
        Node* cur = words;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] =  new Node();
            }

            cur = cur->children[c];
        }
        cur->is_word = true;
    }
    
    bool search(string word) {
        Node* cur = words;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }

            cur = cur->children[c];
        }
        
        return cur->is_word;
    }
    
    bool startsWith(string prefix) {
        Node* cur = words;
        for (char c : prefix) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }

            cur = cur->children[c];
        }
        
        return true;
    }
};
