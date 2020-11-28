function initUi()
  app.registerUi({["menu"] = "Lapis Normal", ["callback"] = "lapisnormal", ["accelerator"] = "<Ctrl>1"});
  app.registerUi({["menu"] = "Lapis Pontilhado", ["callback"] = "lapispontilhado", ["accelerator"] = "<Ctrl>2"});
  app.registerUi({["menu"] = "Seta", ["callback"] = "seta", ["accelerator"] = "<Ctrl>3"});
  app.registerUi({["menu"] = "Marca Texto", ["callback"] = "marcatexto", ["accelerator"] = "<Ctrl>4"});
  app.registerUi({["menu"] = "Reta", ["callback"] = "reta", ["accelerator"] = "<Ctrl>5"});
  app.registerUi({["menu"] = "Texto", ["callback"] = "texto", ["accelerator"] = "<Ctrl>6"});
end


local currentFill = false
local currentSeta = false

function fill()
  currentFill = not currentFill
  app.uiAction({["action"]="ACTION_TOOL_FILL", ["enabled"] = currentFill})
  print("ACTION_TOOL_FILL enabled: " .. tostring(currentFill))
end

local colorList = { 
  {"black", 0x000000},  
  {"green", 0x008000},
  {"lightblue", 0x00c0ff}, 
  {"lightgreen", 0x00ff00}, 
  {"blue", 0x3333cc},      
  {"gray", 0x808080},   
  {"red", 0xff0000},        
  {"magenta", 0xff00ff},
  {"orange", 0xff8000}, 
  {"yellow", 0xffff00},    
  {"white", 0xffffff}
}
local currentColor = 4 -- start with blue color 

local linestyleList = {"PLAIN", "DASH", "DASH_DOT", "DOT"}
local currentLinestyle = 1

local selectList = {"RECT", "REGION", "OBJECT"} -- don't use play selection tool
local currentSelect = 1

local toolList = {"PEN", "ERASER", "HILIGHTER", "SELECTION"}
local currentTool = 1

local eraserList = {"STANDARD", "DELETE_STROKE"} -- I don't use WHITEOUT
local currentEraser = 1

local drawingtypeList = {"TOOL_DRAW_RECT", "TOOL_DRAW_CIRCLE", "TOOL_DRAW_ARROW", "RULER", "TOOL_DRAW_SPLINE", "SHAPE_RECOGNIZER"} -- Don't include coordinate system and default tool
local currentDrawingtype = 1

function lapisnormal()
  app.uiAction({["action"] = "ACTION_TOOL_PEN"})
  app.uiAction({["action"] = "ACTION_TOOL_LINE_STYLE_PLAIN"})
  app.uiAction({["action"]="ACTION_TOOL_DRAW_ARROW", ["enabled"] = false})
  print("ACTION_TOOL_SELECT_" .. selectList[currentSelect])
end

function lapispontilhado()
  app.uiAction({["action"] = "ACTION_TOOL_PEN"})
  app.uiAction({["action"] = "ACTION_TOOL_LINE_STYLE_DOT"})
  app.uiAction({["action"]="ACTION_TOOL_DRAW_ARROW", ["enabled"] = false})
  print("ACTION_TOOL_SELECT_" .. selectList[currentSelect])
end

function marcatexto()
  app.uiAction({["action"] = "ACTION_TOOL_HILIGHTER"})
  app.uiAction({["action"]="ACTION_TOOL_DRAW_ARROW", ["enabled"] = false})
end

function seta()
  app.uiAction({["action"] = "ACTION_TOOL_PEN"})
  app.uiAction({["action"]="ACTION_TOOL_DRAW_ARROW", ["enabled"] = true})
  app.uiAction({["action"] = "ACTION_TOOL_LINE_STYLE_PLAIN"})
  print("ACTION_TOOL_SELECT_" .. selectList[currentSelect])
end

function reta()
  app.uiAction({["action"] = "ACTION_TOOL_PEN"})
  app.uiAction({["action"]="ACTION_RULER", ["enabled"] = true})
  app.uiAction({["action"] = "ACTION_TOOL_LINE_STYLE_PLAIN"})
  print("ACTION_TOOL_SELECT_" .. selectList[currentSelect])
end

function texto()
  app.uiAction({["action"] = "ACTION_TOOL_TEXT"})
end
