import javax.swing.JFrame;
import javax.media.j3d.*;
import javax.vecmath.*;
import com.sun.j3d.utils.universe.*;
import com.sun.j3d.utils.geometry.ColorCube;

public class Simple3D extends JFrame {
    public Simple3D() {
        // Configurer la fenêtre
        setTitle("Simple 3D");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Créer un univers 3D
        SimpleUniverse universe = new SimpleUniverse();
        
        // Créer un groupe de contenu
        BranchGroup group = new BranchGroup();
        
        // Ajouter un cube coloré
        group.addChild(new ColorCube(0.3));
        
        // Configurer la caméra
        universe.getViewingPlatform().setNominalViewingTransform();
        
        // Ajouter le groupe de contenu à l'univers
        universe.addBranchGraph(group);
    }
    
    public static void main(String[] args) {
        // Créer et afficher la fenêtre
        Simple3D window = new Simple3D();
        window.setVisible(true);
    }
}
