package com.mycompany.estudodecaso3jpa;

import dao.EnfermeiroDAO;
import javabeans.Enfermeiro;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

/**
 *
 * @author Enus
 */
public class EstudoDeCaso3JPA {

    public static void main(String[] args) {
        
        /*
        EntityManagerFactory factory = Persistence.createEntityManagerFactory("EstudoDeCaso3JPA_PU");
        EntityManager manager = factory.createEntityManager();
        */
        
        //SALVAR
        
        
        /*
        Enfermeiro enfermeiro1 = new Enfermeiro(1L,"enf","cor","ender",0);
        
        EnfermeiroDAO enfermeirodao = new EnfermeiroDAO();
        enfermeirodao.salvar(enfermeiro1);
        */
        
        //ABRIR
        
        /*
        
        Enfermeiro enfermeiro = new Enfermeiro();
        
        EnfermeiroDAO enfermeirodao = new EnfermeiroDAO();
        
        enfermeiro = (Enfermeiro) enfermeirodao.abrir(1L);
        
        System.out.println(enfermeiro);

        */
        
        //REMOVER
        
        /*
        
        EnfermeiroDAO enfermeirodao = new EnfermeiroDAO();
        enfermeirodao.remover(1L);
        
        */
    }
}
