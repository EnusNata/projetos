package com.mycompany.estudodecaso2jpa;

import dao.MedicoDAO;
import javabeans.Medico;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class EstudoDeCaso2JPA {

    public static void main(String[] args) {
        EntityManagerFactory factory = Persistence.createEntityManagerFactory("EstudoDeCaso2JPA_PU");
        EntityManager manager = factory.createEntityManager();
        
        //Salvar Medico
        
        /*
        Medico medico = new Medico(1L,"paulo","meucrm","osasco - SP");
        
        System.out.println(medico);
        
        manager.getTransaction().begin();
        manager.persist(medico);
        manager.getTransaction().commit();
        
        funcionou
        
        */
        
        
        //Encontrar Medico
        
        /*
        Medico medico = new Medico();
        
        medico = manager.find(Medico.class, 1L);
        
        System.out.println(medico);
        
        funcionou
        
        */
        
        
        //Apagar Medico
        
        /*
        Medico medico = manager.find(Medico.class, 1L);
        
        manager.getTransaction().begin();
        manager.remove(medico);
        manager.getTransaction().commit();
        
        funcionou

        */
        
        //Salvar Medico
        
        /*
        
        Medico medico1 = new Medico(1L,"paulo","meucrm","osasco - SP");
        
        MedicoDAO medicodao = new MedicoDAO();
        
        System.out.println(medicodao.salvar(medico1));
        
        funcionou
        
        */
        
        // Abrir
        
        /*
        
        Medico medico = new Medico();
        
        MedicoDAO medicodao = new MedicoDAO();
        medico = (Medico) medicodao.abrir(1L);
        
        System.out.println(medico);
        
        funcionou
        
        */
        
        //Remover
        
        /*

        Medico medico1 = new Medico(1L,"paulo","meucrm","osasco - SP");
        
        MedicoDAO medicodao = new MedicoDAO();
        medicodao.remover(1L);
        
        funcinou
        
        */
        
    }
    
}
