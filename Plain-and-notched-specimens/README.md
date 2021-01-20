# Theory of critical distances
<p>The Theory of Critical Distances (TCD) is a design method that is widely used in situations of practical interest to estimate the strength of notched/cracked components subjected to either static, dynamic, or fatigue loading. The TCD method was proposed successively by Tanaka and Taylor on the basis of linear elastic fracture mechanics (LEFM). The average stress of a characteristic point or line in the vicinity of the notch is considered in TCD. Failure occurs when the average stress within the distance range from the notch tip exceeds the strength of materials. According to the topology type, TCD can be divided into the following categories, as shown in Figure 1.
 </p>
<p align="center">
  <img src="https://github.com/yanicen1/Theory-of-Critical-Distances/blob/main/Plain-and-notched-specimens/Fig.1.png" width="550" title="hover text">
</p>
<p align="center">
  Figure 1. Different forms of TCD.
</p>
<h4>The Point Method (PM):</h4>
<p><i>σ</i><sub>eff</sub> = <i>σ</i><sub>0</sub></p>
<p><i>σ</i><sub>eff</sub> = <i>σ</i><sub>y</sub> (<i>Ɵ</i>=0, <i>r</i> = <i>L</i>/2)</p>
<p><i>σ</i><sub>y</sub>(<i>r</i>) is a stress-distance discrete curve for the notched specimen. This curve can be obtained by Finite Element Analysis (Ansys, Abaqus, and so on). <i>σ</i><sub>0</sub> is the ultimate strength for the plain specimen (without a notch). L is the critical distance. The purpose is to find L/2 which is the intersection point of <i>σ</i><sub>eff</sub> and <i>σ</i><sub>y</sub>(<i>r</i>).</p>

<h4>The Line Method (LM):</h4>
<p><i>σ</i><sub>eff</sub> = <i>σ</i><sub>0</sub></p>
<p><img src="https://github.com/yanicen1/Theory-of-Critical-Distances/blob/main/Plain-and-notched-specimens/Fig.2.png" width="175"></p>
<p><i>σ</i><sub>y</sub>(<i>r</i>) is a stress-distance discrete curve for the notched specimen. This curve can be obtained by Finite Element Analysis (Ansys, Abaqus, and so on) using the Linear Elastic model. <i>σ</i><sub>0</sub> is the ultimate strength for the plain specimen (without a notch). L is the critical distance. <img src="https://github.com/yanicen1/Theory-of-Critical-Distances/blob/main/Plain-and-notched-specimens/Fig.3.png" width="120"> can be found as the area below the stress-distance curve from 0 to 2L. The purpose is to find 2L.</p>
<br>
<h4>Input:</h4>
<p>1. Change Sigma_0 (Pa) according to your data. Sigma_0 is the stress for the plain specimen (without a notch).</p>
<p>2. Store your data in the file "stress_riser.csv" (Pa vs m). stress_riser.csv contains stress-distance data for the notched specimen. This data can be obtained by Finite Element Analysis (Ansys, Abaqus, and so on).</p>
<p>3. Run the program.</p>
<h4>Output:</h4>
<p>4. The critical distance in mm.</p>
<p>5. The graph that shows stress distribution vs distance from the notch root (Fig. 2).</p>
<p align="center">
  <img src="https://github.com/yanicen1/Theory-of-Critical-Distances/blob/main/Plain-and-notched-specimens/Fig.4.png" width="700" title="hover text">
</p>
<p align="center">
  Figure 2. Stress-distance curves.
</p>
<br>
<p>All used libraries were saved in files 'requirements.txt' and 'environment.yaml' for conda.</p>

More information about TCD you can find in the book "[The Theory of Critical Distances](https://doi.org/10.1016/B978-0-08-044478-9.X5000-5)" by David Taylor, 2007

If you have questions, please feel free to contact me: 
Andrei Iankin, yas.cem.yanicen@gmail.com
