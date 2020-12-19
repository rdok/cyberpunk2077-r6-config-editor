## Installation
- Download `dist.zip`
- Extract `dist/cyberpunk2077-usability.exe` to the cyberpunk 2077 installation directory. 
- Execute said exe file.

## Features
Modifies Cyberpunk 2077 input user mapping to add usability features. Such as button to walk.

#### User Input Mappings

```
"${CYBERPUNK_2077_INSTALLATION_PATH}\r6\config\inputUserMappings.xml"
```

### Hold capslock to move
##### Forward / Back
```
<mapping name="LeftY_Axis" type="Axis" >
  ...
  <button id="IK_CapsLock" val="0" overridableUI="slowWalk"/>
  ...
</mapping>
```

##### Left / Right
```
<mapping name="LeftX_Axis" type="Axis" >
  ...
  <button id="IK_CapsLock" val="0" overridableUI="slowWalk"/>
  ...
</mapping>
```

