# Proposal: [Sudoku]

## Synopsis

[	
The game we're going to try to build is Sudoku, the object of the game is to fill a given 
205	
beginning stage (incomplete 9x9 grid of numbers) with additional numbers so that no number 
206	
appears twice in the same row, column, or sub-grid (one of the 9 3x3 boxes that make up the full grid). 
207	
The interface will be a sprite constructed grid of 81 squares in 9x9 rows and columns. 
208	
We will have two different modes to start the game: easy and hard. 
209	
The easy mode will fill in a set number of squares at random positions with a random number. The hard
210	
mode will do the same except with a larger set number of squares.
211	
]
212	
213	
## Functional requirements
214	
215	
[
216	
 
217	
 1. The User will be prompted to select a game mode before starting the game
218	
 
219	
 1. The user will interact with the board by clicking different squares in the grid and entering their 
220	
    desired number when prompted.
221	
    
222	
 2. The square that the user hovers over will change color to indicate its being chosen
223	
    
224	
 3. The cpu will tell the user if its move is valid, if not it will indicate that by highlighting the cell red
225	
 
226	
 4. The cpu will update the user on how many squares are left
227	
 
228	
 5. The cpu will notify the user if it has hit a dead end in the game
229	
 
230	
 6. The user will be able to quit by pressing a key (prob 'q'.)
231	
 
232	
 7. If the user quits the cpu will return the board to its beginning stage and provide a solution //may remove
233	
 
234	
 8. If the user completes the game the cpu will congratulate the user with Good job!
235	
 
236	
 9. If the user completes the game with hard mode on, the cpu will congratulate the user with Fantastic!
237	
 
238	
 10. The solution that the cpu provides will be provided in red text //may remove
239	
 
240	
 11. The user will be able to undo moves, perhaps by clicking an occupied square and pressing delete
241	
 from a drop down menu
242	
 
243	
 12. The user will not be able to produce errors by interacting with the game
244	
 
245	
 13. The Board will have 9x9 dimensions
246	
 
247	
 14. The user will be able to receive a hint square if it prompts the cpu
248	
 
249	
 15. The user will be able to see the available numbers if it clicks a cell
250	
 
251	
 
252	
 
253	
]
254	
255	
## Open questions
256	
257	
[ 
258	
1. How will I provide the user with a drop down if necessary?
259	
2. What exactly is the best way to determine which members are private?
260	
3. How will I precede the game with a prompt asking the user to choose a mode? 
261	
4. What would be the best way to give the player an option to go a step back?
262	
5. What exactly is the best way to determine when to declare functions with const?
263	
6. What is the "explicit" keyword used for?
264	
7. How do you test a void member function that is meant to be private?
265	
8. What kind of random C++ functions should we use to set up the board? 
266	
9. What's the best way to import a class that is not in the standard library
267	
]