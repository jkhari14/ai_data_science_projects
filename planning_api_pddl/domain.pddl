(define (domain sokorobotto)
  (:requirements :typing :negative-preconditions)
  (:types shipment order location robot pallette saleitem)
  (:predicates (ships ?shipment ?order) (orders ?order ?saleitem) (unstarted ?shipment)
      (packing-location ?location) (available ?location) (contains ?pallette ?saleitem) (free ?robot)
      (connected ?location1 ?location2) (at ?object ?location) (no-robot ?location) (no-pallette ?location)
       (includes ?shipment ?saleitem) (holding ?robot ?pallette) (is-robot ?object) (unblocked ?location))

  (:action move_with_pallette 
  :parameters (?r ?p ?locA ?locB ?si)
  :precondition (and (not (free ?r)) (contains ?p ?si) (at ?r ?locA) (not (packing-location ?locB)) (connected ?locA ?locB) (connected ?locB ?locA) (holding ?r ?p) (no-robot ?locB) (no-pallette ?locB))
  :effect (and (no-robot ?locA ) (not (at ?p ?locA)) (not (at ?r ?locA)) (at ?r ?locB)
            (at ?p ?locB) (not (no-robot ?locB)) (no-pallette ?locA) (not (no-pallette ?locB)) )
    
  )

  (:action move_with_pallette_from_pac 
  :parameters (?r ?p ?locA ?locB ?si)
  :precondition (and (not (free ?r)) (contains ?p ?si) (at ?r ?locA) (not (packing-location ?locB)) (packing-location ?locA) (connected ?locA ?locB) (connected ?locB ?locA) (holding ?r ?p) (no-robot ?locB) (no-pallette ?locB))
  :effect (and  (no-robot ?locA ) (not (at ?p ?locA)) (not (at ?r ?locA)) (at ?r ?locB)
            (at ?p ?locB) (not (no-robot ?locB)) (no-pallette ?locA) (not (no-pallette ?locB)) (available ?locA) )
    
  )

  (:action move_empty_handed
      :parameters (?r ?locA ?locB ?p)
      :precondition (and (not (and (not (no-pallette ?locB) ) (not (at ?p ?locB)) ))  (free ?r)  (at ?r ?locA)  (connected ?locA ?locB) (connected ?locB ?locA) (no-robot ?locB))
      :effect (and (no-robot ?locA ) (not (at ?r ?locA)) (at ?r ?locB) (not (no-robot ?locB)))
  )
  

  (:action move2pac
      :parameters (?r ?p ?locA ?locB)
      :precondition (and (not (free ?r)) (available ?locB) (no-pallette ?locB) (packing-location ?locB) (at ?r ?locA) (connected ?locA ?locB) (connected ?locB ?locA) (holding ?r ?p) (no-robot ?locB))
      :effect (and (not (available ?locB))(not (no-pallette ?locB)) (no-robot ?locA ) (not (at ?p ?locA)) (not (at ?r ?locA)) (at ?r ?locB)
            (at ?p ?locB) (not (no-robot ?locB)) (no-pallette ?locA))
      
  )

  (:action grab
      :parameters (?r ?p ?loc)
      :precondition (and (free ?r) (at ?r ?loc) (at ?p ?loc) )
      :effect (and (not (free ?r)) (holding ?r ?p) )
  )

  (:action load4shipping
      :parameters (?r ?p ?locPac ?o ?ship ?si)
      :precondition (and (at ?r ?locPac) (at ?p ?locPac) (holding ?r ?p) (not (free ?r)) (not (available ?locPac) ) 
                      (packing-location ?locPac) (ships ?ship ?o) (orders ?o ?si) (contains ?p ?si) )
      :effect (and (includes ?ship ?si)  )
  )
  
  (:action release
      :parameters (?r ?p ?loc)
      :precondition (and (at ?r ?loc) (at ?p ?loc) (holding ?r ?p) (not (free ?r)) )
      :effect (and (free ?r) (not (holding ?r ?p)) )
  )
  
  
  


  
)
