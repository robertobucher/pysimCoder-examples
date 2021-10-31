model DisksAndSpring
  Modelica.Mechanics.Rotational.Components.SpringDamper springdamper1(c = 0.4797954, d = 0.0027836) annotation(Placement(visible = true, transformation(origin = {-20, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Damper damper1(d = 0.0002953) annotation(Placement(visible = true, transformation(origin = {-44, -6}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Mechanics.Rotational.Components.Damper damper2(d = 0.0004001) annotation(Placement(visible = true, transformation(origin = {2, -6}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Mechanics.Rotational.Components.Fixed fixed1 annotation(Placement(visible = true, transformation(origin = {-44, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Fixed fixed2 annotation(Placement(visible = true, transformation(origin = {2, -30}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Inertia inertia1(J = 2.223636e-3) annotation(Placement(visible = true, transformation(origin = {-64, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Sensors.AngleSensor anglesensor2 annotation(Placement(visible = true, transformation(origin = {72, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Components.Inertia inertia2(J = 2.218136e-3, stateSelect = StateSelect.never) annotation(Placement(visible = true, transformation(origin = {30, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Blocks.Math.Gain gain2(k = -1) annotation(Placement(visible = true, transformation(origin = {116, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Sources.Torque torque1 annotation(Placement(visible = true, transformation(origin = {-98, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Math.Gain gain1(k = 0.0000382) annotation(Placement(visible = true, transformation(origin = {-136, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput y2 annotation(Placement(visible = true, transformation(origin = {160, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {40, 48}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Mechanics.Rotational.Sensors.AngleSensor anglesensor1 annotation(Placement(visible = true, transformation(origin = {54, 60}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput y1 annotation(Placement(visible = true, transformation(origin = {160, 60}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {208, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealInput u annotation(
    Placement(visible = true, transformation(origin = {-200, 20}, extent = {{-20, -20}, {20, 20}}, rotation = 0), iconTransformation(origin = {-182, 22}, extent = {{-20, -20}, {20, 20}}, rotation = 0)));
equation
  connect(anglesensor1.phi, y1) annotation(
    Line(points = {{65, 60}, {160, 60}}, color = {0, 0, 127}));
  connect(gain2.y, y2) annotation(
    Line(points = {{127, 20}, {160, 20}}, color = {0, 0, 127}));
  connect(anglesensor2.phi, gain2.u) annotation(
    Line(points = {{83, 20}, {104, 20}}, color = {0, 0, 127}));
  connect(inertia2.flange_a, anglesensor2.flange) annotation(
    Line(points = {{40, 20}, {62, 20}}));
  connect(damper2.flange_b, fixed2.flange) annotation(
    Line(points = {{2, -16}, {2, -30}}));
  connect(inertia2.flange_b, damper2.flange_a) annotation(
    Line(points = {{20, 20}, {2, 20}, {2, 4}}));
  connect(inertia1.flange_b, anglesensor1.flange) annotation(
    Line(points = {{-54, 20}, {-44, 20}, {-44, 60}, {44, 60}}));
  connect(gain1.y, torque1.tau) annotation(
    Line(points = {{-125, 20}, {-110, 20}}, color = {0, 0, 127}));
  connect(torque1.flange, inertia1.flange_a) annotation(
    Line(points = {{-88, 20}, {-74, 20}, {-74, 20}, {-74, 20}}));
  connect(springdamper1.flange_b, inertia2.flange_b) annotation(
    Line(points = {{-10, 20}, {20, 20}, {20, 20}, {20, 20}, {20, 20}, {20, 20}}));
  connect(inertia1.flange_b, damper1.flange_a) annotation(
    Line(points = {{-54, 20}, {-46, 20}, {-46, 20}, {-44, 20}, {-44, 12}, {-44, 12}, {-44, 8}, {-44, 8}, {-44, 4}}));
  connect(inertia1.flange_b, springdamper1.flange_a) annotation(
    Line(points = {{-54, 20}, {-30, 20}}));
  connect(damper1.flange_b, fixed1.flange) annotation(
    Line(points = {{-44, -16}, {-44, -16}, {-44, -30}, {-44, -30}, {-44, -30}, {-44, -30}}));
  connect(gain1.u, u) annotation(
    Line(points = {{-148, 20}, {-200, 20}}, color = {0, 0, 127}));
  annotation(experiment(StartTime = 0, StopTime = 10, Tolerance = 1e-6, Interval = 0.02), Diagram(coordinateSystem(extent = {{-400, -400}, {400, 400}}, preserveAspectRatio = true, initialScale = 0.1, grid = {2, 2})), Icon(coordinateSystem(extent = {{-400, -400}, {400, 400}}, preserveAspectRatio = true, initialScale = 0.1, grid = {2, 2})), uses(Modelica(version = "3.2.2")));
end DisksAndSpring;