# Alex Wan 3D Rendering Project
- Alexander Robert Wan
- c2027453
- D3. Computer graphics

## Files Included 
- Python
    - 3DGraphics_c2027453.py
    - data_c2027453.py
    - eulerRotation_c2027453.py
    - facing_c2027453.py
    - quarternion_c2027453.py
    - quicksort_c2027453.py
    - reflection_c2027453.py
    - render_c2027453.py
    - VertexFaceScraper.py
    - 3D_Models
        - Cube.txt
        - maxwellData.txt
        - TeapotData.txt

- html
    - 3DGraphics.html
    - styles.css
    - Images
        - 2DProjection.png
        - EulerRotations.png
        - Perspective.png
        - Quarternion1.png
        - Quarternion2.png
        - QuarternionMult.png
        - ReflectionMatrix.png
    
- README.md

## Program Explanation
To run my program as intended, please run the python file called "3DGraphics_c2027453.py", this will open a pygame window with a cube being the first render. You will notice several GUI settings to use.

The "Auto Spin" will toggle wether the object continues to spin.

The drop down menu in the bottom left allows the user to select different 3D models.

The "Quarternion" button will switch the method of rotation to quarternion, the object will spin about a specified axis, this will be [1,1,1] to begin with.

To change the axis of rotation for the quarternion method enter an x, y and z value for the new axis of rotation in the 3 corresponding boxes above the axis button. Click the axis button to change the axis the 3D model rotates about when in quarternion mode. (Note: if axis boxes are left empty the value for that box will be set to zero).

The position buttons under the heading "position" allow the user to simply move the 3D model by clicking the corresponding button, with there being a + and - option for each axis.

The "Euler" button will switch the method of rotation to Euler rotations, the buttons under the Euler button function the same as the position buttons, however they change the angle of the 3D model about the chosen axis.

Finally the reflection buttons on the middle-right allow the user to toggle a reflected shape, multiple reflections can be used at once.