# class node:
#   def __init__(self, answer_to_go_here, question):
#     self.answer_to_go_here = answer_to_go_here
#     self.question = question
#     self.next_nodes = []

#   def size(self):
#     count = 1 
#     for node in self.next_nodes:
#       count += node.size()  
#     return count

#   def deepth(self):
#     Max = 0
#     for node in self.next_nodes:
#       if node.deepth() > Max:
#         Max = node.deepth()
#     return Max + 1

#   def append(self,question, reponses, question_precedante):
#     if question_precedante == self.question:
#       self.next_nodes.append(node(question, reponses))
#     for n in self.next_nodes:
#       n.append(question, reponses, question_precedante)

# class tree:
#   def __init__(self,question):
#     self.first_node = node("",question)
#     self.current_node = self.first_node

#   def size(self):
#     return self.first_node.size()

#   def deepth(self):
#     return self.first_node.deepth()

#   def append(self, question, reponses, question_precedante):
#     self.first_node.append( question, reponses, question_precedante)

#   def get_question(self):
#     return self.current_node.question
  
class TreeNode:
  def __init__(self, question, yes_node=None, no_node=None, other_node=None, answer=None):
      self.question = question
      self.yes_node = yes_node
      self.no_node = no_node
      self.other_node = other_node
      self.answer = answer
  
  class DiscussionBot:
    def __init__(self):
        # Création de l'arbre de discussion
        self.root = TreeNode("Aimes-tu la pizza ? Perso, c'est mon plat préféré !||réponds avec !rep oui ou non||",
                             yes_node=TreeNode("Laquelles-tu préfères ? Pour ma part, je fonds pour la royale ! ||réponds avec !rep oui ou non||",
                                               other_node=TreeNode("Hmmm.. celle-la est très bonne aussi ! ||réponds avec !rep oui ou non||",
                                                                 other_node=TreeNode("Cool, à plus tard."))),
                             no_node=TreeNode("Tu préfères les lasagnes ? C'est pas mal aussi. ||réponds avec !rep oui ou non||",
                                                                                  other_node=TreeNode("Oh.. le devoir m'appelle, à plus tard !")))

        self.current_node = self.root
        self.topics = set(["nourriture", "lasagnes"])


    def reset_discussion(self):
        self.current_node = self.root
        self.topics = set()

    def process_answer(self, answer):
        if self.current_node.yes_node and answer.lower() in ["yes", "oui"]:
            self.current_node = self.current_node.yes_node
        elif self.current_node.no_node and answer.lower() in ["no", "non"]:
            self.current_node = self.current_node.no_node
        else:
            if self.current_node.other_node:
                self.current_node = self.current_node.other_node
        return self.current_node.question

    def get_response(self):
        if self.current_node.answer:
            return self.current_node.answer
        elif self.current_node.question:
            return self.current_node.question
        else:
            return "Oh.. le devoir m'appelle, à plus tard !"

    def speak_about(self, topic):
        if topic.lower() in self.topics:
            return f"Oui, je parle de {topic}."
        else:
            return f"Non, je ne parle pas de {topic}."